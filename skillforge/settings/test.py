"""
With these settings, tests run faster.
"""

from .base import *  # noqa

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# DATABASE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/topics/testing/overview/#the-test-database
# When using SQLite, the tests will use an in-memory database by default
# (i.e., the database will be created in memory, bypassing the filesystem entirely!).
DATABASES["default"] = {"ENGINE": "django.db.backends.sqlite3"}

# DRF - Django Rest Framework
# ------------------------------------------------------------------------------
# https://www.django-rest-framework.org/api-guide/testing/#setting-the-default-format
REST_FRAMEWORK["TEST_REQUEST_DEFAULT_FORMAT"] = "json"

# Celery
# ------------------------------------------------------------------------------
# As the doc states:
#
# 'The eager mode enabled by the task_always_eager setting is by definition
# not suitable for unit tests.
#
# When testing with eager mode you are only testing an emulation of what
# happens in a worker, and there are many discrepancies between the emulation
# and what happens in reality.'
#
# https://docs.celeryq.dev/en/4.4.3/userguide/testing.html
#
# So later, additionally using pytest-celery in the test suite would be complementary.
# https://docs.celeryq.dev/en/4.4.3/userguide/testing.html#pytest
#
# https://docs.celeryq.dev/en/4.4.3/userguide/configuration.html#task-always-eager
CELERY_ALWAYS_EAGER = True
# https://docs.celeryq.dev/en/4.4.3/userguide/configuration.html#task-eager-propagates
CELERY_EAGER_PROPAGATES = True
