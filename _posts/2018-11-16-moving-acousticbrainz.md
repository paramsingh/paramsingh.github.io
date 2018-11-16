---
layout: post
title: Moving AcousticBrainz
---

_Thoughts on migrating a terabyte scale database to a new server in production for the first time._

In the interest of making this blog an archive of interesting technical work that I do, I'm gonna
write about the recent work I did while migrating the [AcousticBrainz](https://acousticbrainz.org) website
from an old server to MetaBrainz's relatively newer and shinier Hetzner infrastructure.

This was the first time I worked with a production database of this scale, and it was a real learning
experience. It really felt like I had jumped off the deep end, but it was really fun!

Some backstory first, AcousticBrainz is a music technology project which crowd sources acoustic information
for music recordings and is a collaboration between the [Music Technology Group](http://www.mtg.upf.edu/) at
[Universitat Pompeu Fabra](http://www.upf.edu/) and the [MetaBrainz Foundation](https://metabrainz.org). The
project has collected information about 3.7 million unique recordings and has individual submissions from
users for over 11 million recordings. All the data is stored in a single PostgreSQL database for now. The
server that AcousticBrainz used to run on (we called it spike, after the Tom and Jerry character) had gotten
old and started spitting out hard disk failure warnings, so we decided to move it to the central Hetzner
infrastructure where other MetaBrainz projects are hosted.

We use docker for all services running in Hetzner and it has worked pretty well for us so far. So the first
task was [creating a production docker environment](https://github.com/metabrainz/acousticbrainz-server/pull/286)
for AcousticBrainz. Consul is used to provide config values
for the AcousticBrainz server which needed some [new code and consul template files](https://github.com/metabrainz/acousticbrainz-server/pull/284)
to be written. This is relatively simple stuff that did not take too long. We also have a repository to
store all config values and scripts that need to be run on each of our servers. So I also wrote code
to run the three different services that AcousticBrainz needs in different docker containers.

After that, I started work on creating data dumps of the AcousticBrainz data. There was already some code
that dumped the entire database into a lzma compressed file. However, it was old code that hadn't been
run in a long time and the database had gotten biiig since then. The way the code worked was that it
dumped each table as a file into a directory and then added the entire directory at once into a tar file.
However, this approach doesn't work now, because the table that stores the lowlevel json data that users
submit to us has become too big to be stored in a single text file uncompressed. The `lowlevel_json` file
has 11 million rows right now with each row containing a relatively large JSON document stored in
a column of Postgres' cool JSONB type. The table takes around 357 GB when stored inside Postgres and this
balloons to much over the space we had on spike. So, I wrote [code](https://github.com/metabrainz/acousticbrainz-server/pull/293)
that dumped 500,000 rows into a file and compressed it before dumping the next 500,000 rows.

The compressed AcousticBrainz data dump was around 169 GB in size which seemed reasonable. Then, I realized
that the server we were planning to run the webserver on (called boingo, after [Oingo Boingo](https://musicbrainz.org/artist/166bc1cb-a2b7-412d-bcd5-5f439d2cf5f1))
did not have enough storage space
or computational power to hold and work with the database. This led to us getting a new shiny server called frank (after
[Frank Ocean](https://musicbrainz.org/artist/e520459c-dff4-491d-a6e4-c97be35e0044)!) which has a pretty big 7200 RPM hard disk
and over a 100 GB of RAM. We also decided to upgrade to Postgres 10 during the migration, which led me to
[creating a docker image](https://github.com/metabrainz/docker-postgres/pull/5) for PostgreSQL 10 that we
could use in production.

After this, I imported the data into the empty postgres server which worked pretty well. Everything seemed set for
a small downtime for migration where we'd just create a small incremental data dump, move it to frank and import,
bring spike down, bring the webserver up on frank and be done with it. The
[steps](https://docs.google.com/document/d/1uwbKrjqYyId9LaxTs8I3kWXOwDRBm6-eae5NL1uXSrk/edit?usp=sharing) were written
up and we were ready to go.

Things started, I brought the site down on spike, created an incremental dump, imported it to frank. Everything
worked. We decided to do a integrity check of the new database once before bringing the new site up. This is
where the trouble started. The number of rows in one of the the tables was 10 million when it should have
been around a 100M, yikes. We realized that there had been a bug in the original data dump code that
we'd written. It was a pretty small bug, the key we were using to dump the data was incorrect. [One line
fix](https://github.com/metabrainz/acousticbrainz-server/pull/305/files#diff-37702c3ba98fe2366f5df112d1112570R380).
I thought that we need more tests for our data dumps code.

Well, at that point we decided to just go ahead and dump and import the table individually instead of stopping
the whole process. The downtime was much longer than expected because of this, the table was pretty big, 100M rows is no joke,
it took `pg_dump` hours to dump it. Then, I dropped the table on frank and began an import of the dumped file.
We had decided to not drop constraints before importing for sanity reasons, but that turned out to be not
that good an idea. It took the import 5-6 hours before it was even done halfway and the time to import new
rows was increasing. We gave up, stopped the import and dropped all constraints before starting a new
clean import. This worked much much faster and was done in around an hour. At that point, we did another
sanity check of the database, before bringing the site back up.

Some static files like binaries and old dumps we linked to were still hosted on spike (another thing I missed!),
so I had to whip up a quick pull request changing links temporarily. I was doing this at 3 in the morning and
I had started working on this the previous day 11 in the morning. It was the longest, most intense production
deployment I have ever done. Pretty fun, now that I think about it, but I was tired then.

Later, I set up an [FTP server](ftp.acousticbrainz.org) on frank and moved the static files we were hosting there.

There were a lot of things that I learned in this entire process. First thing was that we should really
sanity check literally everything before bringing any production service down. Second thing was that
importing data with constraints in a database (especially for large amounts of data) is not very
feasible. Third is that this level of control is not something that I would ever get as a new grad
in any big company. Being thrown off the deep end here at MetaBrainz was really awesome. Another thing
that I forgot to mention was that the entire migration process was done remotely over IRC with me sitting in college
in Hamirpur, India and my teammates in Barcelona. This really teaches efficient communication and teamwork.

All in all, working with production grade big data projects has been pretty awesome, and I hope I continue
to learn as much as possible as early as possible.
