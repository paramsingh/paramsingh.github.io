---
layout: page
title: Index
---

This is a list of my notes. See <a href="{% link notes/notetaking.md %}">note taking</a>.

{% assign categories = "History, Engineering, Security, Miscellany" | split: ", " %}
{% for category in categories %}
<h3>{{ category }}</h3>
<ul>
{% for note in site.pages %}
    {% if note.url contains "/notes" and note.categories contains category %}
        <li>
            <a href="{{note.url}}">{{ note.title }}</a> 
        </li>
        {% endif %}
    {% endfor %}
    </ul>
{% endfor %}