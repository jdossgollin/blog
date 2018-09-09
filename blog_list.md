---
layout: post
permalink: /allposts/
title: All Blog Posts
---

I post occasionally about interesting news in my professional life, water issues, climate risk, and data analysis.
Posts are sorted below by category

<ul id="archive">
{% capture site_cats %}{% for cat in site.categories %}{{ cat | first }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture %}
{% assign cats_list = site_cats | split:',' | sort %} 

{% for item in (0..site.categories.size) %}
    {% unless forloop.last %}
    {% capture this_word %}{{ cats_list[item] | strip_newlines }}{% endcapture %}
        <article>
            <h2 id="{{ this_word }}" class="tag-heading">
                {{ this_word }}
            </h2>
            <ul id="archive">
                {% for post in site.categories[this_word] %}
                    {% if post.title != null %}
                        <li>
                            <a href="{{ site.baseurl }}{{ post.url }}" title="{{ post.title }}">
                                {{ post.title }}
                            </a> ({{post.date | date: "%d %B %Y"}})
                            <p>
                            {{ post.content | strip_html | truncatewords: 45 }}
                            </p>
                        </li>
                    {% endif %}
                {% endfor %}
            </ul>
        </article>
    {% endunless %}
{% endfor %}
</ul>

<!--[{{post.title}}]({{ site.baseurl }}{{ post.url }})  
____  
-->