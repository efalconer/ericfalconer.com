#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Eric Falconer'
SITENAME = "Eric Falconer (Don't overthink it)"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/efalconer/'),
          ('Github', 'https://github.com/efalconer'),
          ('Twitter', 'https://twitter.com/efalconer'),
          ('Instagram', 'https://www.instagram.com/efalconer/'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = [
    'images', 
    'extra/robots.txt', 
    'extra/favicon.ico',
    'extra/icon.svg',
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/icon.svg': {'path': 'icon.svg'},
}

TWITTER_USERNAME='efalconer'

THEME='theme'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
