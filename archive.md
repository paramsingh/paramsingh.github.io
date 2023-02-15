---
layout: post
title: Archive
permalink: /archive/
---

This list of blog posts used to be on the main page. I've started writing on [newsletter.param.codes](https://newsletter.param.codes)
so I repurposed the main page to be an introduction. This is the archive of those old blog posts.

There is also [the diary page](/diary) for old longer, more personal updates.

<section class="post-list">
  <div class="container">
    {% for post in site.posts %}
      {% unless post.next %}
        <h2 class="category-title">{{ post.date | date: '%Y' }}</h2>
      {% else %}
        {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
        {% capture nyear %}{{ post.next.date | date: '%Y' }}{% endcapture %}
        {% if year != nyear %}
          <h2 class="category-title">{{ post.date | date: '%Y' }}</h2>
        {% endif %}
      {% endunless %}
      <article class="post-item">
        <span class="post-meta date-label">{{ post.date | date: "%b %d" }}</span>
        <div class="article-title"><a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></div>
      </article>
    {% endfor %}
  </div>
</section>
