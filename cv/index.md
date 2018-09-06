---
layout: plain
title: Curriculum Vitae
---

# {{ site.data.main.contact.name }}
{{ site.data.main.contact.title }}  
{{ site.data.main.contact.department }}  
{{ site.data.main.contact.institution }}  

## Contact ##
{{ site.data.main.contact.email }}  
[{{ site.data.main.contact.website }}]({{ site.data.main.contact.website }})

## Education ##
{% for edu in site.data.main.education %}
* _{{ edu.dates}}_ -- __{{ edu.degree }}__, {{ edu.institution }}, {{ edu.location }}
{% endfor %}

## Appointments ##
{% for apt in site.data.main.appointments %}
* _{{ apt.dates}}_ -- __{{ apt.title }}__, {{ apt.institution }}, {{ apt.location }}    
{% endfor %}

## Awards ##
{% for award in site.data.awards %}
*  {{ award.institution }} _{{ award.name }}_ ({{ award.date }})
{% endfor %}

## Teaching

{% for course in site.data.teaching %}
*  {{ course.role }} for {{ course.number }}: _{{ course.name }}_, {{ course.instructor }}, {{ course.size }} students. ({{ course.semester }})
{% endfor %}

## Skills ##

### Languages

{% for lang in site.data.language %}
* {{ lang.name }} ({{ lang.level }})
{% endfor %}

### Computer Skills

{% for skill in site.data.skills %}
* **{{ skill.name }}**: {{ skill.description }}
{% endfor %}

## Service ##

### Peer Review ###

Please see [my Publons page](publons.com/a/1468228/) for a complete list of verified reviews.
{% for item in site.data.service.review %}
* {{ item.time }}: {{ item.journal }}
{% endfor %}

### Profesional ###
{% for item in site.data.service.professional %}
* {{ item.time }}: {{ item.position }}, {{ item.organization }}
{% endfor %}

### Outreach ###
{% for item in site.data.service.outreach %}
* {{ item.time }}: {{ item.position }}, {{ item.organization }}
{% endfor %}

## Publications & Presentations ##

### Peer-Reviewed Articles ###
{% bibliography  --query @article %}

### In Preparation / Under Review
{% bibliography --query @unpublished %}

### Conference Presentations ###
{% bibliography  --query @inproceedings %}

### Invited Talks ###
{% assign invitedtalks = site.data.presentations.invited | sort: 'date' | reverse %}
{% for pres in invitedtalks %}
* {{ pres.date }}: _{{ pres.title }}_, {{ pres.location }}. {% if pres.pdf %} &rarr; [PDF]({{ pres.pdf }}){% endif %} {% if pres.link %}[link]({{ pres.link }}){% endif %}
{% endfor %}

### Workshop Presentations ###
{% assign workshoptalks = site.data.presentations.workshop | sort: 'date' | reverse %}
{% for pres in workshoptalks %}
* {{ pres.date }}: _{{ pres.title }}_, {{ pres.location }}. {% if pres.pdf %} &rarr; [PDF]({{ pres.pdf }}){% endif %} {% if pres.link %}[link]({{ pres.link }}){% endif %}
{% endfor %}