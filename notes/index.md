---
layout: page
title: Index
categories: [Miscellany]
---

This is a list of my notes. See <a href="{% link notes/notetaking.md %}">note taking</a>.

<ul>
{% for category in site.categories %}
    <h3> {{ category[0] }} </h3>
    {% for note in categories[1] %}
        {% if note.url contains "/notes" %}
        <li>
            <a href="{{note.url}}">{{ note.title }}</a>
        </li>
        {% endif %}
    {% endfor %}
{% endfor %}
</ul>
