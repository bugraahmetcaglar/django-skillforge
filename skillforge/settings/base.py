"""
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                                  │
│  ____                             _    _                    _      ____            _             │
│ | __ ) _   _  __ _ _ __ __ _     / \  | |__  _ __ ___   ___| |_   / ___|__ _  __ _| | __ _ _ __  │
│ |  _ \| | | |/ _` | '__/ _` |   / _ \ | '_ \| '_ ` _ \ / _ \ __| | |   / _` |/ _` | |/ _` | '__| │
│ | |_) | |_| | (_| | | | (_| |  / ___ \| | | | | | | | |  __/ |_  | |__| (_| | (_| | | (_| | |    │
│ |____/ \__,_|\__, |_|  \__,_| /_/   \_\_| |_|_| |_| |_|\___|\__|  \____\__,_|\__, |_|\__,_|_|    │
│              |___/                                                           |___/               │
│                                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
Django settings for skillforge project.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from datetime import timedelta
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getattr(os.environ, ("SECRET_KEY"), "django-insecure-(q_xc+d@c4wzz0@80)nraq&7k^^*@yhj-_8h$a5ax!d0zpgfi$")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG")

ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL = "user.User"

# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_swagger",
    "rest_framework_simplejwt",
    "django_filters",
    "drf_yasg",
    "ckeditor",
]

LOCAL_APPS = [
    "core.blog",
    # "core.question",
    # "core.support",
    "core.user",
    # "core.video",
]

if DEBUG:
    THIRD_PARTY_APPS += [
        "django_extensions",
    ]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "skillforge.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "skillforge.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
    }
}

# CACHE
# ------------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://redis:7000/1",  # "redis://redis:7000/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

CKEDITOR_UPLOAD_PATH = "/media/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CORS
# ------------------------------------------------------------------------------
CORS_ALLOW_METHODS = ("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS")

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = (
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "sentry-trace",
)


# Celery
# ------------------------------------------------------------------------------
# BROKER_URL = os.environ.get("BROKER_URL", "amqp://guest:guest@localhost//")

# LOGGING
# ------------------------------------------------------------------------------
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOG_FORMAT = "[%(asctime)s] [%(levelname)-7s] [%(module)s %(name)s (%(lineno)d)] %(message)s"
LONG_LOG_FORMAT = "[%(asctime)s] [%(levelname)-7s] [p:%(process)d th:%(thread)d | m:%(module)s n:%(name)s ln:(%(lineno)d)] %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S%z"
LOG_LEVEL = os.getenv("DJANGO_LOG_LEVEL", "WARNING")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": LOG_FORMAT,
            "datefmt": LOG_DATE_FORMAT,
        },
        "simple": {
            "format": "[%(asctime)s %(levelname)s %(module)s] %(message)s",
            "datefmt": LOG_DATE_FORMAT,
        },
        "verbose": {
            "format": LONG_LOG_FORMAT,
            "datefmt": LOG_DATE_FORMAT,
        },
    },
    "filters": {
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"},
        "require_debug_true": {"()": "django.utils.log.RequireDebugTrue"},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "default" if LOG_LEVEL != "DEBUG" else "verbose",
        },
        "console_simple": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "filters": ["require_debug_true"],
            "formatter": "simple",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "root": {
        "level": os.getenv("ROOT_LOG_LEVEL", LOG_LEVEL),
        "handlers": ["console"],
    },
    "loggers": {
        "django": {
            "level": LOG_LEVEL,
            "handlers": ["console", "mail_admins"],
            "propagate": False,
        },
        "django.request": {
            "level": LOG_LEVEL,
            "propagate": True,
        },
        "django.server": {
            "level": LOG_LEVEL,
            "propagate": True,
        },
        "django.db.backends": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console", "mail_admins"],
            "propagate": True,
        },
    },
}


SWAGGER_SETTINGS = {
    "is_authenticated": True,
    "is_superuser": True,
    "SECURITY_DEFINITIONS": {"api_key": {"type": "apiKey", "in": "header", "name": "Authorization"}},
}

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAdminUser",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
}

JWT_AUTH = {
    "JWT_ENCODE_HANDLER": "rest_framework_jwt.utils.jwt_encode_handler",
    "JWT_DECODE_HANDLER": "rest_framework_jwt.utils.jwt_decode_handler",
    "JWT_PAYLOAD_HANDLER": "rest_framework_jwt.utils.jwt_payload_handler",
    "JWT_PAYLOAD_GET_USER_ID_HANDLER": "rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler",
    "JWT_RESPONSE_PAYLOAD_HANDLER": "rest_framework_jwt.utils.jwt_response_payload_handler",
    "JWT_SECRET_KEY": "SECRET_KEY",
    "JWT_GET_USER_SECRET_KEY": None,
    "JWT_PUBLIC_KEY": None,
    "JWT_PRIVATE_KEY": None,
    "JWT_ALGORITHM": "HS256",
    "JWT_VERIFY": True,
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LEEWAY": 0,
    "JWT_EXPIRATION_DELTA": timedelta(days=30),
    "JWT_AUDIENCE": None,
    "JWT_ISSUER": None,
    "JWT_ALLOW_REFRESH": False,
    "JWT_REFRESH_EXPIRATION_DELTA": timedelta(days=30),
    "JWT_AUTH_HEADER_PREFIX": "Bearer",
    "JWT_AUTH_COOKIE": None,
}
