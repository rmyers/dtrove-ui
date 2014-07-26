from __future__ import absolute_import

# The celery app must be loaded here to make the @shared_task decorator work.
from .celery import app as celery_app
