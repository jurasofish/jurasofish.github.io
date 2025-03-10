AUTHOR = 'Michael Jurasovic'
SITENAME = 'Michael Jurasovic'
SITEURL = "https://jurasofish.github.io"

PATH = "content"

TIMEZONE = 'Australia/Melbourne'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Github', 'https://github.com/jurasofish'),
)

# Social widget
SOCIAL = (
    ('Github', 'https://github.com/jurasofish'),
)

MENUITEMS = (
    ('GitHub', 'https://github.com/jurasofish'),
)

DEFAULT_PAGINATION = False

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
PYGMENTS_STYLE = 'xcode'
CUSTOM_CSS = 'static/css/custom.css'
STATIC_PATHS = [
    'extra',
]
EXTRA_PATH_METADATA = {'extra/custom.css': {'path': 'static/css/custom.css'}}
HIDE_SIDEBAR = True
PADDED_SINGLE_COLUMN_STYLE = True
DISPLAY_CATEGORIES_ON_MENU = False
RELATIVE_URLS = True
