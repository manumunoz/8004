import os
from os import environ

import dj_database_url

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True

# don't share this with anybody.
SECRET_KEY = 'mgz=n2r#zx412)_-r57o%7158(zdxopg1fc9_i1lk@54lvcqrz'


DATABASES = {
    'default': dj_database_url.config(
        # Rather than hardcoding the DB parameters here,
        # it's recommended to set the DATABASE_URL environment variable.
        # This will allow you to use SQLite locally, and postgres/mysql
        # on the server
        # Examples:
        # export DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
        # export DATABASE_URL=mysql://USER:PASSWORD@HOST:PORT/NAME

        # fall back to SQLite if the DATABASE_URL env var is missing
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'testuser'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True



# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree',]

SENTRY_DSN = environ.get('SENTRY_DSN')

DEMO_PAGE_INTRO_TEXT = """
<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            oTree on GitHub
        </a>.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            oTree homepage
        </a>.
    </li>
</ul>
<p>
    Here are various games implemented with oTree. These games are all open
    source, and you can modify them as you wish.
</p>
"""

ROOMS = [
    {
        'name': 'econ101',
        'display_name': 'Econ 101 class',
        'participant_label_file': '_rooms/econ101.txt',
    },
    {
        'name': 'live_demo',
        'display_name': 'Room for live demo (no participant labels)',
    },
]


mturk_hit_settings = {
    'keywords': ['bonus', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': []
}


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.01,
    'participation_fee': 0.50,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}

SESSION_CONFIGS = [
    # ---------------------------------------#
    # -------------  THIRD  -----------------#
    # ---------------------------------------#

    {
        'name': 'switch_p1_third',
        'display_name': "switch_p1_third",
        'num_demo_participants': 7,
        'app_sequence': ['switch_p1_third'],
    },

    # --------------------------------------------#
    # -------------  TREATMENTS  -----------------#
    # --------------------------------------------#
    {
        'name': 'full_spanish',
        'display_name': "full_spanish",
        'num_demo_participants': 7,
        'app_sequence': ['cambio_inst_p1', 'cambio_p1','cambio_inst_p2', 'cambio_p2'],
        'treatment': 1,
        # 'use_browser_bots': True
    },
    {
        'name': 'sticky_spanish',
        'display_name': "sticky_spanish",
        'num_demo_participants': 7,
        'app_sequence': ['cambio_inst_p1', 'cambio_p1', 'cambio_inst_p2', 'cambio_p2'],
        'treatment': 2,
    },
    {
        'name': 'blurry_spanish',
        'display_name': "blurry_spanish",
        'num_demo_participants': 7,
        'app_sequence': ['cambio_inst_p1', 'cambio_p1', 'cambio_inst_p2', 'cambio_p2'],
        'treatment': 3,
    },
    {
        'name': 'full_english',
        'display_name': "full_english",
        'num_demo_participants': 7,
        'app_sequence': ['switch_inst_p1', 'switch_p1', 'switch_inst_p2', 'switch_p2'],
        'treatment': 1,
    },
    {
        'name': 'sticky_english',
        'display_name': "sticky_english",
        'num_demo_participants': 7,
        'app_sequence': ['switch_inst_p1', 'switch_p1', 'switch_inst_p2', 'switch_p2'],
        'treatment': 2,
    },
    {
        'name': 'blurry_english',
        'display_name': "blurry_english",
        'num_demo_participants': 7,
        'app_sequence': ['switch_inst_p1', 'switch_p1', 'switch_inst_p2', 'switch_p2'],
        'treatment': 3,
    },

    #--------------------------------------------#
    #--------------   PART 1   ------------------#
    #--------------------------------------------#
    # {
    #     'name': 'cambio_inst_p1',
    #     'display_name': "cambio_inst_p1",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['cambio_inst_p1'],
    # },
    # {
    #     'name': 'cambio_p1',
    #     'display_name': "cambio_p1",
    #     'num_demo_participants': 7,
    #     'app_sequence': ['cambio_p1'],
    # },
    # {
    #     'name': 'switch_inst_p1',
    #     'display_name': "switch_inst_p1",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['switch_inst_p1'],
    # },
    {
        'name': 'switch_p1',
        'display_name': "switch_p1",
        'num_demo_participants': 7,
        'app_sequence': ['switch_p1'],
    },
    #--------------------------------------------#
    #--------------   PART 2   ------------------#
    #--------------------------------------------#
    # {
    #     'name': 'cambio_inst_p2_t1',
    #     'display_name': "cambio_inst_p2_t1",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['cambio_inst_p2'],
    #     'treatment': 1,
    # },
    # {
    #     'name': 'cambio_inst_p2_t2',
    #     'display_name': "cambio_inst_p2_t2",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['cambio_inst_p2'],
    #     'treatment': 2,
    # },
    # {
    #     'name': 'cambio_inst_p2_t3',
    #     'display_name': "cambio_inst_p2_t3",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['cambio_inst_p2'],
    #     'treatment': 3,
    # },
    # {
    #     'name': 'cambio_p2_t1',
    #     'display_name': "cambio_p2_t1",
    #     'num_demo_participants': 7,
    #     'app_sequence': ['cambio_p2'],
    #     'treatment': 1,
    # },
    # {
    #     'name': 'cambio_p2_t2',
    #     'display_name': "cambio_p2_t2",
    #     'num_demo_participants': 7,
    #     'app_sequence': ['cambio_p2'],
    #     'treatment': 2,
    # },
    # {
    #     'name': 'cambio_p2_t3',
    #     'display_name': "cambio_p2_t3",
    #     'num_demo_participants': 7,
    #     'app_sequence': ['cambio_p2'],
    #     'treatment': 3,
    # },
    # {
    #     'name': 'switch_inst_p2_t1',
    #     'display_name': "switch_inst_p2_t1",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['switch_inst_p2'],
    #     'treatment': 1,
    # },
    # {
    #     'name': 'switch_inst_p2_t2',
    #     'display_name': "switch_inst_p2_t2",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['switch_inst_p2'],
    #     'treatment': 2,
    # },
    # {
    #     'name': 'switch_inst_p2_t3',
    #     'display_name': "switch_inst_p2_t3",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['switch_inst_p2'],
    #     'treatment': 3,
    # },
    {
        'name': 'switch_p2_t1',
        'display_name': "switch_p2_t1",
        'num_demo_participants': 7,
        'app_sequence': ['switch_p2'],
        'treatment': 1,
    },
    # {
    #     'name': 'switch_p2_t2',
    #     'display_name': "switch_p2_t2",
    #     'num_demo_participants': 7,
    #     'app_sequence': ['switch_p2'],
    #     'treatment': 2,
    # },
    # {
    #     'name': 'switch_p2_t3',
    #     'display_name': "switch_p2_t3",
    #     'num_demo_participants': 7,
    #     'app_sequence': ['switch_p2'],
    #     'treatment': 3,
    # },
]

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
