from __future__ import absolute_import

import os

from celery import Celery
from blog.settings import base

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings.dev")

app = Celery("blog")

app.config_from_object("blog.settings.dev", namespace="CELERY"),

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)