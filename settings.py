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

ADMIN_USERNAME = 'admin'
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

# SENTRY_DSN = ''

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
    {
        'name': 'p1_frst3',
        'display_name': "p1_frst3",
        'num_demo_participants': 8,
        'app_sequence': ['p1_frst3'],
        'treatment': '1',
    },
    {
        'name': 'p1_no3',
        'display_name': "p1_no3",
        'num_demo_participants': 8,
        'app_sequence': ['p1_no3'],
        'treatment': '2',
    },
    {
        'name': 'p1_exo3',
        'display_name': "p1_exo3",
        'num_demo_participants': 8,
        'app_sequence': ['p1_exo3'],
        'treatment': '3',
    },
    {
        'name': 'p1_endo3',
        'display_name': "p1_endo3",
        'num_demo_participants': 8,
        'app_sequence': ['p1_endo3'],
        'treatment': '4',
    },
    {
        'name': 'p1_vctm3',
        'display_name': "p1_vctm3",
        'num_demo_participants': 8,
        'app_sequence': ['p1_vctm3'],
        'treatment': '5',
    },
    {
        'name': 'p2_frst3',
        'display_name': "p2_frst3",
        'num_demo_participants': 8,
        'app_sequence': ['p2_frst3'],
        'treatment': '1',
    },
    {
        'name': 'p2_no3',
        'display_name': "p2_no3",
        'num_demo_participants': 8,
        'app_sequence': ['p2_no3'],
        'treatment': '2',
    },
    {
        'name': 'p2_exo3',
        'display_name': "p2_exo3",
        'num_demo_participants': 8,
        'app_sequence': ['p2_exo3'],
        'treatment': '3',
    },
    {
        'name': 'p2_endo3',
        'display_name': "p2_endo3",
        'num_demo_participants': 8,
        'app_sequence': ['p2_endo3'],
        'treatment': '4',
    },
    {
        'name': 'p2_vctm3',
        'display_name': "p2_vctm3",
        'num_demo_participants': 8,
        'app_sequence': ['p2_vctm3'],
        'treatment': '5',
    },
    {
        'name': 'p3_frst3',
        'display_name': "p3_frst3",
        'num_demo_participants': 8,
        'app_sequence': ['p3_frst3'],
        'treatment': '1',
    },
    {
        'name': 'p3_no3',
        'display_name': "p3_no3",
        'num_demo_participants': 8,
        'app_sequence': ['p3_no3'],
        'treatment': '2',
    },
    {
        'name': 'p3_exo3',
        'display_name': "p3_exo3",
        'num_demo_participants': 8,
        'app_sequence': ['p3_exo3'],
        'treatment': '3',
    },
    {
        'name': 'p3_endo3',
        'display_name': "p3_endo3",
        'num_demo_participants': 8,
        'app_sequence': ['p3_endo3'],
        'treatment': '4',
    },
    {
        'name': 'p3_vctm3',
        'display_name': "p3_vctm3",
        'num_demo_participants': 8,
        'app_sequence': ['p3_vctm3'],
        'treatment': '5',
    },
    {
        'name': 'three_p1',
        'display_name': "three_p1",
        'num_demo_participants': 48,
        'app_sequence': ['three_p1'],
    },
    # {
    #     'name': 'three_p1_T1_FRST',
    #     'display_name': "three_p1_T1_FRST",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p1'],
    #     'treatment': '1',
    # },
    # {
    #     'name': 'three_p1_T2_NO',
    #     'display_name': "three_p1_T2_NO",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p1'],
    #     'treatment': '2',
    # },
    # {
    #     'name': 'three_p1_T3_EXO',
    #     'display_name': "three_p1_T3_EXO",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p1'],
    #     'treatment': '3',
    # },
    # {
    #     'name': 'three_p1_T4_ENDO',
    #     'display_name': "three_p1_T4_ENDO",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p1'],
    #     'treatment': '4',
    # },
    # {
    #     'name': 'three_p1_T5_VCTM',
    #     'display_name': "three_p1_T5_VCTM",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p1'],
    #     'treatment': '5',
    # },
    # {
    #     'name': 'three_p1_T11_VCTM5',
    #     'display_name': "three_p1_T11_VCTM5",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p1'],
    #     'treatment': '11',
    # },
    # {
    #     'name': 'three_p2',
    #     'display_name': "three_p2",
    #     'num_demo_participants': 48,
    #     'app_sequence': ['three_p2'],
    # },
    # {
    #     'name': 'three_p2_T1_FRST',
    #     'display_name': "three_p2_T1_FRST",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p2'],
    #     'treatment': '1',
    # },
    # {
    #     'name': 'three_p2_T2_NO',
    #     'display_name': "three_p2_T2_NO",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p2'],
    #     'treatment': '2',
    # },
    # {
    #     'name': 'three_p2_T3_EXO',
    #     'display_name': "three_p2_T3_EXO",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p2'],
    #     'treatment': '3',
    # },
    # {
    #     'name': 'three_p2_T4_ENDO',
    #     'display_name': "three_p2_T4_ENDO",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p2'],
    #     'treatment': '4',
    # },
    # {
    #     'name': 'three_p2_T5_VCTM',
    #     'display_name': "three_p2_T5_VCTM",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p2'],
    #     'treatment': '5',
    # },
    # {
    #     'name': 'three_p2_T11_VCTM5',
    #     'display_name': "three_p2_T11_VCTM5",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p2'],
    #     'treatment': '11',
    # },
    # {
    #     'name': 'three_p3',
    #     'display_name': "three_p3",
    #     'num_demo_participants': 6,
    #     'app_sequence': ['three_p3'],
    # },
    # {
    #     'name': 'three_p3_T1_FRST',
    #     'display_name': "three_p3_T1_FRST",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p3'],
    #     'treatment': '1',
    # },
    # {
    #     'name': 'three_p3_T2_NO',
    #     'display_name': "three_p3_T2_NO",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p3'],
    #     'treatment': '2',
    # },
    # {
    #     'name': 'three_p3_T3_EXO',
    #     'display_name': "three_p3_T3_EXO",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p3'],
    #     'treatment': '3',
    # },
    # {
    #     'name': 'three_p3_T4_ENDO',
    #     'display_name': "three_p3_T4_ENDO",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p3'],
    #     'treatment': '4',
    # },
    # {
    #     'name': 'three_p3_T5_VCTM',
    #     'display_name': "three_p3_T5_VCTM",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p3'],
    #     'treatment': '5',
    # },
    # {
    #     'name': 'three_p3_T11_VCTM5',
    #     'display_name': "three_p3_T11_VCTM5",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p3'],
    #     'treatment': '11',
    # },
    # {
    #     'name': 'three_p4_T5_VCTM',
    #     'display_name': "three_p4_T5_VCTM",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p4'],
    #     'treatment': '5',
    # },
    # {
    #     'name': 'three_p4_T11_VCTM5',
    #     'display_name': "three_p4_T11_VCTM5",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p4'],
    #     'treatment': '11',
    # },
    # {
    #     'name': 'three_p5_T11_VCTM5',
    #     'display_name': "three_p5_T11_VCTM5",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['three_p5'],
    #     'treatment': '11',
    # },
    # {
    #     'name': 'two_p1',
    #     'display_name': "two_p1",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['two_p1'],
    # },
    {
        'name': 'two_p1_T6_FRST',
        'display_name': "two_p1_T6_FRST",
        'num_demo_participants': 8,
        'app_sequence': ['two_p1'],
        'treatment': '6',
    },
    {
        'name': 'two_p1_T7_NO',
        'display_name': "two_p1_T7_NO",
        'num_demo_participants': 8,
        'app_sequence': ['two_p1'],
        'treatment': '7',
    },
    {
        'name': 'two_p1_T8_EXO',
        'display_name': "two_p1_T8_EXO",
        'num_demo_participants': 8,
        'app_sequence': ['two_p1'],
        'treatment': '8',
    },
    {
        'name': 'two_p1_T9_ENDO',
        'display_name': "two_p1_T9_ENDO",
        'num_demo_participants': 8,
        'app_sequence': ['two_p1'],
        'treatment': '9',
    },
    {
        'name': 'two_p1_T10_VCTM',
        'display_name': "two_p1_T10_VCTM",
        'num_demo_participants': 8,
        'app_sequence': ['two_p1'],
        'treatment': '10',
    },
    {
        'name': 'two_p2',
        'display_name': "two_p2",
        'num_demo_participants': 8,
        'app_sequence': ['two_p2'],
    },
    # {
    #     'name': 'import_test',
    #     'display_name': "import_test",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['import_test'],
    # },
    # {
    #     'name': 'MTurk_Study_P2',
    #     'display_name': "MTurk: P2",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['lie_P2'],
    # },
    # {
    #     'name': 'MTurk_NO_low_P2',
    #     'display_name': "MTurk: NO Low P2",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['lie_P2'],
    #     'treatment':'1',
    # },
    # {
    #     'name': 'MTurk_NO_high_P2',
    #     'display_name': "MTurk: NO high P2",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['lie_P2'],
    #     'treatment':'2',
    # },
    # {
    #     'name': 'MTurk_EXO_low_P2',
    #     'display_name': "MTurk: EXO Low P2",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['lie_P2'],
    #     'treatment':'3',
    # },
    # {
    #     'name': 'MTurk_EXO_high_P2',
    #     'display_name': "MTurk: EXO high P2",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['lie_P2'],
    #     'treatment':'4',
    # },
    # {
    #     'name': 'MTurk_ENDO_low_P2',
    #     'display_name': "MTurk: ENDO Low P2",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['lie_P2'],
    #     'treatment':'5',
    # },
    # {
    #     'name': 'MTurk_ENDO_high_P2',
    #     'display_name': "MTurk: ENDO high P2",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['lie_P2'],
    #     'treatment':'6',
    # },
    # {
    #     'name': 'MTurk_VCTM_low_P2',
    #     'display_name': "MTurk: VCTM Low P2",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['lie_P2'],
    #     'treatment':'7',
    # },
    # {
    #     'name': 'MTurk_VCTM_high_P2',
    #     'display_name': "MTurk: VCTM high P2",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['lie_P2'],
    #     'treatment':'8',
    # },
    # {
    #     'name': 'MTurk_Study_P3',
    #     'display_name': "MTurk: P3",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['lie_P3'],
    # },
    # {
    #     'name': 'MTurk_NO_low_P3',
    #     'display_name': "MTurk: NO Low P3",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['lie_P3'],
    #     'treatment':'1',
    # },
    # {
    #     'name': 'MTurk_NO_high_P3',
    #     'display_name': "MTurk: NO high P3",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['lie_P3'],
    #     'treatment':'2',
    # },
    # {
    #     'name': 'MTurk_EXO_low_P3',
    #     'display_name': "MTurk: EXO Low P3",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['lie_P3'],
    #     'treatment':'3',
    # },
    # {
    #     'name': 'MTurk_EXO_high_P3',
    #     'display_name': "MTurk: EXO high P3",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['lie_P3'],
    #     'treatment':'4',
    # },
    # {
    #     'name': 'MTurk_ENDO_low_P3',
    #     'display_name': "MTurk: ENDO Low P3",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['lie_P3'],
    #     'treatment':'5',
    # },
    # {
    #     'name': 'MTurk_ENDO_high_P3',
    #     'display_name': "MTurk: ENDO high P3",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['lie_P3'],
    #     'treatment':'6',
    # },
    # {
    #     'name': 'MTurk_VCTM_low_P3',
    #     'display_name': "MTurk: VCTM Low P3",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['lie_P3'],
    #     'treatment':'7',
    # },
    # {
    #     'name': 'MTurk_VCTM_high_P3',
    #     'display_name': "MTurk: VCTM high P3",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['lie_P3'],
    #     'treatment':'8',
    # },
    # {
    #     'name': 'MTurk_Study_P4',
    #     'display_name': "MTurk: P4",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['lie_P4'],
    # },
    # {
    #     'name': 'lie_CTRL_Low',
    #     'display_name': "Lie CTRL (Low)",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['lie_CTRL'],
    #     'treatment':'0',
    # },
    # {
    #     'name': 'lie_CTRL_High',
    #     'display_name': "Lie CTRL (High)",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['lie_CTRL'],
    #     'treatment':'1',
    # },
    # {
    #     'name': 'lie_NO_P1',
    #     'display_name': "Lie NO P1",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['lie_NO_P1'],
    # },
    # {
    #     'name': 'lie_no_13',
    #     'display_name': "Lie NO(13)",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['lie_no_13'],
    # },
    # {
    #     'name': 'lie_exo_13',
    #     'display_name': "Lie EXO(13)",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['lie_exo_13'],
    # },
    # {
    #     'name': 'lie_endo_13',
    #     'display_name': "Lie ENDO(13)",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['lie_endo_13'],
    # },
    # {
    #     'name': 'lie_vctm_13',
    #     'display_name': "Lie VCTM(13)",
    #     'num_demo_participants': 4,
    #     'app_sequence': ['lie_vctm_13'],
    # },
    # {
    #     'name': 'lie_no_53',
    #     'display_name': "Lie NO(53)",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['lie_no_53'],
    # },
    # {
    #     'name': 'lie_exo_53',
    #     'display_name': "Lie EXO(53)",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['lie_exo_53'],
    # },
    # {
    #     'name': 'network_study',
    #     'display_name': "network_study",
    #     'num_demo_participants': 4,
    #     'app_sequence': ['network_study'],
    # },
    # {
    #     'name': 'net_formation',
    #     'display_name': "net_formation",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['net_formation'],
    # },
    # {
    #     'name': 'web_of_lies',
    #     'display_name': "Web of Lies",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['web_of_lies'],
    # },
    # {
    #     'name': 'diversity',
    #     'display_name': "Diversity",
    #     'num_demo_participants': 4,
    #     'app_sequence': ['diversity'],
    # },
    # {
    #     'name': 'min_effort',
    #     'display_name': "Min. Effort",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['min_effort'],
    # },
    # {
    #     'name' : 'canvas',
    #     'display_name' : "canvas",
    #     'num_demo_participants' : 4,
    #     'app_sequence' : ['canvas'],
    # },
    # {
    #     'name': 'id_switch',
    #     'display_name': "ID Switch",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['id_switch'],
    # },
    # {
    #     'name' : 'matrixgman',
    #     'display_name' : "Matrixgman",
    #     'num_demo_participants' : 1,
    #     'app_sequence' : ['matrixgman', 'final'],
    # },
    {
        'name': 'word_task',
        'display_name': "Word Task",
        'num_demo_participants': 1,
        'app_sequence': ['word_task', 'final'],
    },
    # {
    #     'name': 'sum_task',
    #     'display_name': "Sum Task",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['sum_task', 'final'],
    # },
    # {
    #     'name' : 'test_qualtrix',
    #     'display_name' : "Test Qualtrix",
    #     'num_demo_participants' : 12,
    #     'app_sequence' : ['qualtrix', 'matrixgman', 'qualtrix2'],
    # },
    # {
    #     'name' : 'payment_info',
    #     'display_name' : "Payment info",
    #     'num_demo_participants' : 1,
    #     'app_sequence' : ['payment_info'],
    # },
    # {
    #     'name' : 'attached_en',
    #     'display_name' : "Attachment Survey English",
    #     'num_demo_participants' : 1,
    #     'app_sequence' : ['attached_en',],
    # },
    # {
    #     'name' : 'attached',
    #     'display_name' : "Attachment",
    #     'num_demo_participants' : 1,
    #     'app_sequence' : ['attached',],
    # },
    # {
    #     'name' : 'qualtrix',
    #     'display_name' : "Qualtrix",
    #     'num_demo_participants' : 1,
    #     'app_sequence' : ['qualtrix'],
    # },
    # {
    #     'name' : 'qualtrix2',
    #     'display_name' : "Qualtrix2",
    #     'num_demo_participants' : 1,
    #     'app_sequence' : ['qualtrix', 'qualtrix2'],
    # },
   # {
   #      'name' : 'matrix',
   #      'display_name' : "Matrix",
   #      'num_demo_participants' : 2,
   #      'app_sequence' : ['matrix'],
   #  },
   #  {
   #      'name': 'Lying_game',
   #      'display_name': "Lying game",
   #      'num_demo_participants': 2,
   #      'app_sequence': ['Lying_game'],
   #  },
    # {
    #     'name': 'public_goods',
    #     'display_name': "Public Goods",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['public_goods', 'payment_info'],
    # },
    # {
    #     'name': 'trust',
    #     'display_name': "Trust Game",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['trust', 'payment_info'],
    # },
    # {
    #     'name': 'guess_two_thirds',
    #     'display_name': "Guess 2/3 of the Average",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['guess_two_thirds', 'payment_info'],
    # },
    # {
    #     'name': 'survey',
    #     'display_name': "Survey",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['survey', 'payment_info'],
    # },
    # {
    #     'name': 'quiz',
    #     'display_name': "Quiz",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['quiz'],
    # },
    # {
    #     'name': 'prisoner',
    #     'display_name': "Prisoner's Dilemma",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['prisoner', 'payment_info'],
    # },
    # {
    #      'name': 'ultimatum',
    #      'display_name': "Ultimatum (randomized: strategy vs. direct response)",
    #      'num_demo_participants': 2,
    #      'app_sequence': ['ultimatum', 'payment_info'],
    # },
    # {
    #     'name': 'ultimatum_strategy',
    #     'display_name': "Ultimatum (strategy method treatment)",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['ultimatum', 'payment_info'],
    #     'use_strategy_method': True,
    # },
    # {
    #     'name': 'ultimatum_non_strategy',
    #     'display_name': "Ultimatum (direct response treatment)",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['ultimatum', 'payment_info'],
    #     'use_strategy_method': False,
    # },
    # {
    #     'name': 'vickrey_auction',
    #     'display_name': "Vickrey Auction",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['vickrey_auction', 'payment_info'],
    # },
    # {
    #     'name': 'volunteer_dilemma',
    #     'display_name': "Volunteer's Dilemma",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['volunteer_dilemma', 'payment_info'],
    # },
    # {
    #     'name': 'cournot',
    #     'display_name': "Cournot Competition",
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'cournot', 'payment_info'
    #     ],
    # },
    # {
    #     'name': 'principal_agent',
    #     'display_name': "Principal Agent",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['principal_agent', 'payment_info'],
    # },
    # {
    #     'name': 'dictator',
    #     'display_name': "Dictator Game",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['dictator', 'payment_info'],
    # },
    # {
    #     'name': 'matching_pennies',
    #     'display_name': "Matching Pennies",
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'matching_pennies',
    #     ],
    # },
    # {
    #     'name': 'traveler_dilemma',
    #     'display_name': "Traveler's Dilemma",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['traveler_dilemma', 'payment_info'],
    # },
    # {
    #     'name': 'bargaining',
    #     'display_name': "Bargaining Game",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['bargaining', 'payment_info'],
    # },
    # {
    #     'name': 'common_value_auction',
    #     'display_name': "Common Value Auction",
    #     'num_demo_participants': 3,
    #     'app_sequence': ['common_value_auction', 'payment_info'],
    # },
    # {
    #     'name': 'stackelberg',
    #     'display_name': "Stackelberg Competition",
    #     'real_world_currency_per_point': 0.01,
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'stackelberg', 'payment_info'
    #     ],
    # },
    # {
    #     'name': 'bertrand',
    #     'display_name': "Bertrand Competition",
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'bertrand', 'payment_info'
    #     ],
    # },
    # {
    #     'name': 'real_effort',
    #     'display_name': "Real-effort transcription task",
    #     'num_demo_participants': 1,
    #     'app_sequence': [
    #         'real_effort',
    #     ],
    # },
    # {
    #     'name': 'lemon_market',
    #     'display_name': "Lemon Market Game",
    #     'num_demo_participants': 3,
    #     'app_sequence': [
    #         'lemon_market', 'payment_info'
    #     ],
    # },
    # {
    #     'name': 'battle_of_the_sexes',
    #     'display_name': "Battle of the Sexes",
    #     'num_demo_participants': 2,
    #     'app_sequence': [
    #         'battle_of_the_sexes', 'payment_info'
    #     ],
    # },
]

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
