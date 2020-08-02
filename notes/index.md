---
layout: page
title: Index
---

This is a list of my notes. See <a href="{% link notes/notetaking.md %}">{% link notes/notetaking.md %}</a>.

Kindle highlights: <a href="{% link highlights/index.md %}">{% link highlights/index.md %}</a>

{% assign categories = "History, Engineering, Security, Miscellany" | split: ", " %}
{% for category in categories %}

<h3>{{ category }}</h3>

<table>
    {% for note in site.pages %}
    {% if note.url contains "/notes" and note.categories contains category %}
    <tr>
        <td> {{note.title}} </td>
        <td><a href="{{note.url}}">{{ note.url }}</a></td>
    </tr>
    {% endif %}
    {% endfor %}
</table>
{% endfor %}
