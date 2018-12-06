#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITETITLE = 'Water & Climate Risk Blog'
SITESUBTITLE = 'by James Doss-Gollin'
AUTHOR = 'James Doss-Gollin'
SITENAME = 'Blog'
SITEDESCRIPTION = 'Personal and research blog of James Doss-Gollin'

# Update this value in publishconf.py with the published site
SITEURL = 'http://localhost:8000/'
PATH = 'content'
TIMEZONE = 'America/New_York'
STATIC_PATHS = ['images', 'extras/CNAME', 'extras/library.bib']

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('My CV', 'https://github.com/jdossgollin/fullcv/blob/master/CV_Doss-Gollin_James.pdf'),
)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/jdossgollin'),
    ('twitter', 'https://twitter.com/jdossgollin'),
    ('linkedin', 'https://www.linkedin.com/in/jamesdossgollin/'),
    ('researchgate', 'https://www.researchgate.net/profile/James_Doss-Gollin')
)


DEFAULT_PAGINATION = 10

# PLUGINS AND SETTINGS
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = [
    'pelican-cite',
    'ipynb.markup',
    'pelican_youtube',
    'render_math',
]
MARKUP = ('md', 'ipynb', 'rst')
IPYNB_USE_METACELL = True
PUBLICATIONS_SRC = 'content/extras/library.bib'

# THEME AND SETUP
THEME = 'pelican-themes/Flex'
SITELOGO = SITEURL + '/images/james.jpg'
COPYRIGHT_YEAR = 2018
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