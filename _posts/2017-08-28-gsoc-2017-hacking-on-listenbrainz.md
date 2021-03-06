---
layout: post
title: GSoC 2017 - Hacking on ListenBrainz
---

This post was originally written for the [MusicBrainz blog](https://blog.musicbrainz.org/2017/08/29/gsoc-2017-hacking-on-listenbrainz/). I wrote it as a report explaining the work I did during Google Summer of Code.

---

Namaste!

I am Param Singh, an undergraduate at the National Institute of Technology, Hamirpur, India, and I worked on ListenBrainz over the summer as part of the Google Summer of Code program. I started contributing code to ListenBrainz in January 2017 and have been working on new features and bug fixes since. I’ll be writing about the work I did and my experience working on LB in this blog post.

After a few of my patches had made it in and I was comfortable with the ListenBrainz codebase (which was a really nice example of software architecture for me), I talked with the LB team about what possible contributions I could make over the summer, and we decided that a Google BigQuery based statistics system is something that would be useful to have in ListenBrainz after we release a beta and have listen data that is permanently archived. I made a [proposal](https://community.metabrainz.org/t/gsoc-2017-adding-statistics-and-graphs-to-listenbrainz/227733) for adding statistics to ListenBrainz which got accepted! During the community bonding period, we decided to try to get a solid and stable beta of ListenBrainz released before starting with the relatively large code additions that would be required by my project proposal. We tracked issues that we wanted fixed before a release in the MetaBrainz ticket tracker [here](https://tickets.metabrainz.org/projects/LB/versions/10621). This work of fixing release blocking issues went into the coding period and we decided to continue working on a solid beta instead of adding new features for the time being. 

I started with fixing bugs and adding new features to get a beta released as soon as possible. Some cool stuff I worked on during this time was dockerizing MessyBrainz (see PR [here](https://github.com/metabrainz/messybrainz-server/pull/18)), migrating the codebases of MessyBrainz and ListenBrainz to Python 3 (PRs [here](https://github.com/metabrainz/listenbrainz-server/pull/187) and [here](https://github.com/metabrainz/messybrainz-server/pull/20)) and improving the startup resilience of various parts of ListenBrainz to make sure that the server is able to self-heal (partially) if some part of it like RabbitMQ goes down (ticket [here](https://tickets.metabrainz.org/browse/LB-155)). 

Later on, I did a big refactor of the LB code so that adding new modules would be easier in the future (PR [here](https://github.com/metabrainz/listenbrainz-server/pull/179)). I also spent a lot of time fixing bugs in our listen deduplication. Relevant pull requests for this are [here](https://github.com/metabrainz/listenbrainz-server/pull/212) and [here](https://github.com/metabrainz/listenbrainz-server/pull/223).

Another feature I added to ListenBrainz while working on the beta was incremental imports. Earlier, LB didn’t keep track of previous imports of a user and did a full Last.FM import every time. However, now we keep track of the last time each user imported listens and only import new data since then. The PR adding incremental imports is [here](https://github.com/metabrainz/listenbrainz-server/pull/207).

My mentor, Robert Kaye (ruaok) set up a test instance of the ListenBrainz server that was used by the community and as the community kept throwing their data at us, bugs kept popping up. A particularly weird bug caused LB to lose data for users with special characters in their usernames. The [PR](https://github.com/metabrainz/listenbrainz-server/pull/199) to fix this took a lot of time to create. 

We kept on fixing bugs for a long time and the biggest thing I took away from this period of GSoC was the [Ninety-ninety rule](https://en.wikipedia.org/wiki/Ninety-ninety_rule), "The first 90 percent of the code accounts for the first 90 percent of the development time. The remaining 10 percent of the code accounts for the other 90 percent of the development time." This summer has drilled this into my mind.

As soon as the beta was released, I started with writing code for statistics, making schema changes (PR [here](https://github.com/metabrainz/listenbrainz-server/pull/192)) and adding some user stats (PRs [here](https://github.com/metabrainz/listenbrainz-server/pull/202) and [here](https://github.com/metabrainz/listenbrainz-server/pull/244)). I’ll be continuing on the stats work after Summer of Code. The basic foundation of stats is mostly done and soon I’ll start with showing statistics to the users.

By the end of the official GSoC coding period, I have made 266 commits in the ListenBrainz [codebase](https://github.com/metabrainz/listenbrainz-server/graphs/contributors) and have opened a total of [111 pull requests](https://github.com/metabrainz/listenbrainz-server/pulls?utf8=%E2%9C%93&q=author%3Aparamsingh). The current production ListenBrainz running on [https://listenbrainz.org](https://listenbrainz.org) has 253 commits by me, most of which were made during the GSoC period. 

Over the summer, I have fallen in love with the MetaBrainz community and have learned a lot of stuff. I’m really looking forward to adding more features to ListenBrainz soon, so that the data that the community is contributing becomes useful to everyone. I loved working on a really cool open-source project like ListenBrainz this summer and am very thankful to Google for providing me this opportunity. I would encourage everyone reading this to give the ListenBrainz beta a try and contribute to ListenBrainz if possible.

