"""
Django settings for barsuart project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url
load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_URL = '/media/'

# The directory where media files are saved on the server
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3)hx(k=!ptcd68ydz&%i-=er8x@i82l4e3%9vq%p!3+e7de^0x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't', 'yes')

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ['barsenetart.com', 'www.barsenetart.com']

if DEBUG == False:
    SECURE_SSL_REDIRECT = True
# Application definition

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "ERROR",  # Change to DEBUG for more verbosity
    },
    "django": {
        "handlers": ["console"],
        "level": "ERROR",
        "propagate": True,
    },
}


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'originals',
    'aboutme',
    'order',
    'contactme',
    'backgroundvid'
]
 # or 'bootstrap5' if you're using Bootstrap 5
SITE_ID = 1
# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # or any other email service you use
EMAIL_PORT = 587  # Port for sending email (for Gmail)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')  # Your email address
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')  # Your email password (or app password for Gmail)
DEFAULT_TO_EMAIL = os.getenv('DEFAULT_TO_EMAIL')   # Default from email for outgoing emails

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'barsuart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Add this line
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

WSGI_APPLICATION = 'barsuart.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

if DEBUG:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    }
else:
    DATABASES = {
        'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
    }



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Optional: Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

CLOUDINARY = {
  'cloud_name' : os.getenv('CLOUD_NAME'),
  'api_key' : os.getenv('CLOUDINARY_API_KEY'),
  'api_secret' : os.getenv('CLOUDINARY_API_SECRET'),
  'secure': True
}

