#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Michael Jurasovic'
SITENAME = 'jurasofish.github.io'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Australia/Melbourne'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

OUTPUT_PATH = 'docs/'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    'pelican.plugins.render_math',
    'i18n_subsites',
]

THEME = 'themes/pelican-bootstrap3'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# BOOTSTRAP_THEME = 'flatly'
BOOTSTRAP_THEME = 'yeti'
PYGMENTS_STYLE = 'emacs'
# CUSTOM_CSS = r'static\custom.css'
# STATIC_PATHS = ['images', r'extra\custom.css']
# EXTRA_PATH_METADATA = {r'extra\custom.css': {'path': r'static\custom.css'}}
