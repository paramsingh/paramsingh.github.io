---
layout: page
title: Code Review
categories:
  - Engineering
---

It's widely known that code review is important for improving the quality of a code base and for
helping engineers improve their skills and share knowledge across the engineering organization.

However, it wasn't obvious to me initially, that in sufficiently large organizations, good code
review practices are neccessary for reliability and security purposes. If engineers can
make bespoke changes to a large codebase without review, it won't be long before someone makes
a broken change to a critical part of the codebase without realizing that they're causing a
breakage or adding a security hole.

Google has the concept of code owners, meaning each directory has an assigned list of owners, and
changes in each directory require a sign-off from the owner of that directory before that change
is merged. This helps in reliability for sure, because it guarantees that an incident doesn't
happen because someone made a change to a part of the codebase without having enough context on the
code. It also helps security because it increases the number of people who need to signoff on
changes and limits the people who CAN approve a PR to a smaller list of people.
