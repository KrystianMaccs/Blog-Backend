from .base import *



# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config("POSTGRES_ENGINE"),
        'NAME': config("POSTGRES_DB"),
        'USER': config("POSTGRES_USER"),
        'PASSWORD': config("POSTGRES_PASSWORD"),
        'HOST': config("PG_HOST"),
        'PORT': config("PG_PORT"),
    }
}

# Email SMTP Settings

EMAIL_HOST = config("EMAIL_HOST")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_PORT = config("EMAIL_PORT")

# Celery Config
CELERY_BROKER_URL = config("CELERY_BROKER")
CELERY_RESULT_BACKEND = config("CELERY_BACKEND")
CELERY_TIMEZONE = "Africa/Lagos"