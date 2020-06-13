"""
Django settings for hack21 project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
# import user


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yq85+kmg8v4m0c1c&l$jg%)mpgj_-9_nbq0u=&xzxwj+h2h*9o'

import django
# django.setup()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#email backends
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend '

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'user',
    'accounts',
    'allauth', #Google social auth
    'allauth.account', #Google social auth
    'allauth.socialaccount', #Google social auth
    'allauth.socialaccount.providers.google', #google auth
    'social_django', #gh, fb auth
    'profiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware', #social auth
]

ROOT_URLCONF = 'hack21.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',  #social auth
                'social_django.context_processors.login_redirect',  #social auth
            ],
        },
    },
]

WSGI_APPLICATION = 'hack21.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

#Static files config
STATIC_URL = '/static/'

STATICFILES_DIRS = [
os.path.join(BASE_DIR, 'static'),
]



AUTH_USER_MODEL='accounts.Account' #custom user model

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2', #GitHub Auth
    'social_core.backends.twitter.TwitterOAuth', #Twitter Auth
    'social_core.backends.facebook.FacebookOAuth2', #Facebook Auth

    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend', #allauth for google auth
 )

SITE_ID = 1 
# LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'



#Social auth

#Google
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

#GitHub
SOCIAL_AUTH_GITHUB_KEY = 'af28583955286523de58'
SOCIAL_AUTH_GITHUB_SECRET = '6cdaa56dad33092cef90a4b7817cfbe08ea05269'
SOCIAL_AUTH_GITHUB_SCOPE =['user']

#Twitter -> Not functioning
SOCIAL_AUTH_TWITTER_KEY = 'BCcr62lglIFzXArJzgdDgZJxg'
SOCIAL_AUTH_TWITTER_SECRET = 'p1zdhfYE11OiJhPYWD4V38UdIrBfSzmcl36LOvE7mjCcOqXrqn'
SOCIAL_AUTH_TWITTER_SCOPE =['user']

#Facebook
SOCIAL_AUTH_FACEBOOK_KEY = '209821926705333'  
SOCIAL_AUTH_FACEBOOK_SECRET = '8ebc15783ebf1cfcbdd626502d1f6f9c'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email'] 
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {       
  'fields': 'email'
}
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [                 
    ('email', 'email'),
]