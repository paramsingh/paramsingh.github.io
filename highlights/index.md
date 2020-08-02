---
layout: page
title: Index
---

Importing my kindle highlights here.

<ul>
{% for page in site.pages %}
    {% if page.url contains "/highlights" %}
    <li>
        <a href="{{page.url}}">{{ page.title }}</a>
    </li>
    {% endif %}
{% endfor %}
</ul>
