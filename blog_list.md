---
layout: post
permalink: /allposts/
title: All Blog Posts
---

I blog occasionally about floods, flood risk, coding, or other cool stuff
A full listing of my blog posts follows.

{% for post in site.posts %}

### [{{post.title}}]({{ site.baseurl }}{{ post.url }})  
#### {{post.date | date: "%d %B %Y"}}
<p>
    {{ post.content | strip_html | truncatewords: 65 }}
</p>

{% endfor %}