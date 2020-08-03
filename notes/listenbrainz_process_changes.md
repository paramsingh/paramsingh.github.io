---
backlinks:
  being_a_mentor: Being a GSoC mentor
categories:
- Engineering
layout: post
title: ListenBrainz release process changes
---

Over the past year, I've made a major change in how we think about releases for [ListenBrainz](https://listenbrainz.org).

## Before

There were no real expectations around deployment after pull requests got merged.
There were two branches -- `master` and `production`. The HEAD of `production` is
what the site was running at any moment. People made pull requests based off `master`, stuff got merged into `master`
and _eventually_ got released.

Each release required merging master into production. However, there may have been hotfixes to production in the meanwhile
as well. So what we ended up doing to bring master and production into sync was:

1. Merge `master` into `production`.
2. Deploy the `production` branch.
3. Merge `production` back into `master`.

The time between releases could be months! The commit difference between master and production
was often in the order of hundreds. This made releases painful and we had to be extra careful. If there
was a schema change involved, that made things even more complicated.

## After

The change that we made is merging stuff into master as often as possible. And as soon as it's merged, release
the changes into production. This set up a decent pipeline where each release consisted of a small number of pull requests,
making it much easier to release stuff.

Over the last 3 months, we've done 33 releases (almost 3 deploys a week), which account for ~400 commits.

There have been a number of advantages to this approach. The deployer doesn't feel as concerned releasing 1 small pull
request vs releasing 100 huge pull requests merged into master a few months ago. It also sets up a quick feedback loop
for the developer who gets to see their changes working in real life as soon as their pull request gets merged.

Given our engineering capacity, this new method of releasing stuff often has really helped in making ListenBrainz
a more active project.