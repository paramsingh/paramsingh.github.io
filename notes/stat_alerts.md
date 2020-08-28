---
layout: post
title: Alert Fatigue
categories:
  - Engineering
---

Notes from this tech talk [[^0]] by Aditya Mukherjee.

# STAT framework for thinking about each alert

- Supported
- Trustworthy
  - Do I trust this alert to notify me when a problem happens?
  - Will it stay silent if things are ok?
  - Will it give me enough info to diagnose problems?
- Actionable
  - At most one decision should be required ideally, the decision to whether take an action or not.
  - Alerts that are difficult to action become alerts that are ignored. If an alert is painful or annoying to action, you'll feel fatigued next time.
  - Should try to avoid stuff like "investigate" etc, make things more optional. Decision trees, interactive tooling etc is much better.
  - If it's unclear who should be taking action, the alert is not actionable.
- Triaged

[^0]: https://vimeo.com/274820572
