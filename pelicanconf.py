#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITETITLE = 'Climate Risk Blog'
SITESUBTITLE = 'by James Doss-Gollin'
AUTHOR = 'James Doss-Gollin'
SITENAME = 'James Doss-Gollin'
SITEDESCRIPTION = 'Personal and research blog of James Doss-Gollin'

# Update this value in publishconf.py with the published site
SITEURL = 'http://localhost:8000'
PATH = 'content'
TIMEZONE = 'America/New_York'
STATIC_PATHS = ['images', 'extra/library.bib', 'pdf']

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('My Homepage', 'https://jamesdossgollin.me'),
    ('My CV', 'https://jamesdossgollin.me/cv-pdf/CV_Doss-Gollin_James.pdf'),
)

# Social widget
SOCIAL = (
    ('envelope', 'mailto:james.doss-gollin@gmail.com'),
    ('github', 'https://github.com/jdossgollin'),
    ('twitter', 'https://twitter.com/jdossgollin'),
    ('linkedin', 'https://www.linkedin.com/in/jamesdossgollin/'),
)

DEFAULT_PAGINATION = 10

# PLUGINS AND SETTINGS
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = [
    'ipynb.markup',
    'render_math',
    'pelican-cite',
    'pelican_youtube',
    'liquid_tags.gram'
]
MARKUP = ('md', 'ipynb', 'rst')
IPYNB_USE_METACELL = True
PUBLICATIONS_SRC = 'content/extra/library.bib'

USE_LESS = True

# THEME AND SETUP
THEME = 'pelican-themes/Flex'
SITELOGO = SITEURL + '/images/james.jpg'
COPYRIGHT_YEAR = 2019
COPYRIGHT_NAME = 'James Doss-Gollin'
BROWSER_COLOR = '#333333'
OG_LOCALE = 'en/US'
MAIN_MENU = True
MENUITEMS = (
    ('Archives', 'archives.html'),
    ('Categories', 'categories.html'),
    ('Tags', 'tags.html'),
)
PAGES_SORT_ATTRIBUTE = 'title'
DISABLE_URL_HASH = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True