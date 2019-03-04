import warnings
from .base import *

# CORS to allow external apps auth through OAuth 2
# https://github.com/ottoyiu/django-cors-headers

INSTALLED_APPS += (
    'corsheaders',
)

MIDDLEWARE_CORS = [
    'corsheaders.middleware.CorsMiddleware',
]

MIDDLEWARE = MIDDLEWARE_CORS + MIDDLEWARE

CORS_ORIGIN_WHITELIST = os.environ['CORS_ORIGIN_WHITELIST'].split(',')


# Security
# https://docs.djangoproject.com/en/1.11/ref/settings/#allowed-hosts

try:
    ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(',')
except KeyError:
    ALLOWED_HOSTS = []


# Logging
# https://docs.djangoproject.com/en/1.11/topics/logging/#configuring-logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

# NGINX and HTTPS
# https://docs.djangoproject.com/en/1.11/ref/
# settings/#std:setting-USE_X_FORWARDED_HOST

USE_X_FORWARDED_HOST = True if os.getenv('USE_X_FORWARDED_HOST') == 'True' \
    else False

# https://docs.djangoproject.com/en/1.11/ref/settings/#secure-proxy-ssl-header

if os.getenv('USE_HTTPS') == 'True':
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
