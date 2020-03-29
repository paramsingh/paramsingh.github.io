---
layout: page
title: Index
---

This is a list of my notes. See <a href="{% link notes/notetaking.md %}">note taking</a>.

<ul>
{% for note in site.pages %}
    {% if note.url contains "/notes" %}
    <li>
        <a href="{{note.url}}">{{ note.title }}</a>
    </li>
    {% endif %}
{% endfor %}
</ul>
