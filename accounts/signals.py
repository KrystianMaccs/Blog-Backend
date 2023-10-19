import logging

from django.db.models.signals import post_save
from django.dispatch import receiver
from blog.settings.base import AUTH_USER_MODEL
from .tasks import fetch_and_save_geodata, fetch_and_save_holiday_data

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def trigger_celery_tasks(sender, instance, created, **kwargs):
    if created:
        fetch_and_save_geodata.delay()
        fetch_and_save_holiday_data.delay(instance.id)
        logger.info(f"{instance}'s profile created")
