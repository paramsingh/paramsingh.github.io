---
layout: post
title: Threat Modeling
---
A threat model is a living artifact that helps us reason about the security of a system.

Threat modeling helps define system appropriate security requirements and helps
find security issues that might not be found otherwise. For example, it is impossible
for automated tools to realize that some flow needs authorization.

A threat model should contain the following things:

* Some form of system diagram -- Anything will do as long as long as it helps us understand the system.
* List of viable threats -- Viable is key here, because there could be an infinite number of possible threats.
* List of prioritized mitigations done or planned
* List of assumptions made

There are methods that can be used to come up with threats:

* [STRIDE]({% link notes/stride.md %})
* Abuser stories 
* Threat Lists ([CAPEC]())
* Vulnerability Lists ([OWASP Top 10]() etc)

Mitigation can involve many things, some of which are as follows:

* Authorization
* Auditing and Logging
* Authentication
* Communication Security
* Configuration Management
* Cryptography
* Exception Management
* Input validation
* Handling sensitive data correctly