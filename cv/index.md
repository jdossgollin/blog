---
layout: plain
title: Curriculum Vitae
---

# {{ site.data.main.contact.name }}
{{ site.data.main.contact.title }}
{{ site.data.main.contact.department }}  
{{ site.data.main.contact.institution }}  

## Contact ##
[{{ site.data.main.contact.email }}](mailto:{{ site.data.main.contact.email }})  
[{{ site.data.main.contact.website }}]({{ site.data.main.contact.website }})

## Education ##
{% assign myschools = site.data.main.education | sort: 'sdate' | reverse %}
{% for edu in myschools %}
* __{{ edu.sdate | date: "%B %Y" }} -- {% if edu.edate %}{{ edu.edate | date: "%B. %Y" }}{%else%}Present{% endif %}__: _{{ edu.degree }}_, {{ edu.institution }}, {{ edu.location }}
{% endfor %}

## Experience ##
{% assign myexperience = site.data.main.appointments | sort: 'sdate' | reverse %}
{% for apt in myexperience %}
* __{{ apt.sdate | date: "%B %Y" }} -- {% if apt.edate %}{{ apt.edate | date: "%B. %Y" }}{%else%}Present{% endif %}__: _{{ apt.title }}_. {{ apt.institution }}, {{ apt.location }}.    
{% endfor %}

## Awards ##
{% for award in site.data.awards %}
*  __{{ award.date }}__:
        {% if award.link %}[_{{ award.name }}_,]({{ award.link }}){:target="_blank"}
        {% else %}_{{ award.name }}_,
        {% endif %} {{ award.institution }}.
{% endfor %}

## Teaching

{% for course in site.data.teaching %}
*  __{{ course.semester }}__: {{ course.role }} for {{ course.number }}: _{{ course.name }}_, {{ course.instructor }}, {{ course.size }} students.
{% endfor %}

## Skills ##

### Languages

{% for lang in site.data.language %}
* __{{ lang.name }}__: {{ lang.level }}
{% endfor %}

### Computer Skills

{% for skill in site.data.skills %}
* **{{ skill.name }}**: {{ skill.description }}
{% endfor %}

## Service ##

### Peer Review ###

Please see [my Publons page](https://publons.com/a/1468228/){:target="_blank"} for a complete list of verified reviews.
{% for item in site.data.service.review %}
* __{{ item.time }}__: {{ item.journal }}
{% endfor %}

### Profesional ###
{% for item in site.data.service.professional %}
* __{{ item.time }}__: _{{ item.position }}_, {{ item.organization }}
{% endfor %}

### Outreach ###
{% for item in site.data.service.outreach %}
* __{{ item.time }}__: _{{ item.position }}_, {{ item.organization }}
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
* __{{ pres.date }}__: _{{ pres.title }}_.  
    {{ pres.location }}{% if pres.format %} ({{ pres.format }}) {% endif %}.
    {% if pres.pdf %}<a href='{{ site.data.main.contact.website }}{{ pres.pdf }}' target='_blank'>
            <i class="fa fa-file-pdf-o"></i>
        </a>
    {% endif %}
    {% if pres.link %}<a href='{{ site.data.main.contact.website }}{{ pres.link }}' target='_blank'>
            <i class="fa fa-external-link"></i>
        </a>
    {% endif %}
{% endfor %}

### Workshop Presentations ###

{% assign workshoptalks = site.data.presentations.workshop | sort: 'date' | reverse %}
{% for pres in workshoptalks %}
* __{{ pres.date }}__: _{{ pres.title }}_.  
    {{ pres.location }}{% if pres.format %} ({{ pres.format }}) {% endif %}.
    {% if pres.pdf %}<a href='{{ site.data.main.contact.website }}{{ pres.pdf }}' target='_blank'>
            <i class="fa fa-file-pdf-o"></i>
        </a>
    {% endif %}
    {% if pres.link %}<a href='{{ site.data.main.contact.website }}{{ pres.link }}' target='_blank'>
            <i class="fa fa-external-link"></i>
        </a>
    {% endif %}
{% endfor %}