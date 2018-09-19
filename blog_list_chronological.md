---
layout: post
permalink: /allpostschron/
title: All Blog Posts
---

I post occasionally about interesting news in my professional life, water issues, climate risk, and data analysis.
The following posts are sorted below by year; to see a list of posts sorted by topic [click here](/allposts/)

<ul id="archive">
    {% for post in site.posts %}
        {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
        {% if year != y %}
            {% assign year = y %}
            <h2 class="blogyear">{{ y}}</h2>
        {% endif %}
        <li>
            <strong>
                <a href="{{ site.baseurl }}{{ post.url }}" title="{{ post.title }}">
                    {{ post.title }}
                </a> ({{post.date | date: "%d %B %Y"}})
            </strong>
            <br/>
            <i>
                {{ post.excerpt | strip_html }}
            </i>
            <a href="{{ post.url }}">Read more</a>
        </li>
    {% endfor %}
</ul>