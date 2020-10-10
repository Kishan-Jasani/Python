'''
settings.py:-
-------------
We need to add our application name inside INSTALLED_APPS list present inside settings.py


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'testapp'
]


we need to add templates folder inside main project if we want to add HTML files
we have to add below path inside settings.py
--------------------------------------------
import os
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')


Now,
add TEMPLATE_DIR inside DIRS list

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]




we have to add below path and below list inside settings.py to use images and css
----------------------------------------------------------------------------------

STATIC_DIR = os.path.join(BASE_DIR,'static')

STATICFILES_DIRS = [ STATIC_DIR ]

'''