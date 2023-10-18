# import logging

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from blog.settings.base import AUTH_USER_MODEL
# from .tasks import populate_user_geo_data

# logger = logging.getLogger(__name__)


# @receiver(post_save, sender=AUTH_USER_MODEL)
# def handle_user_created(sender, instance, created, **kwargs):
#     if created:
#         # Trigger Celery tasks to populate user geo data and check for holidays
#         populate_user_geo_data.delay(instance.id)
#         logger.info(f"{instance}'s profile created")
#         print("User geo data has been generated.")
#         #check_for_holiday.delay(instance.id)


import requests
from decouple import config
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserGeoData

from blog.settings.base import AUTH_USER_MODEL


@receiver(post_save, sender=AUTH_USER_MODEL)
def fetch_and_save_ip_and_country(sender, instance, created, **kwargs):
    if created:
        #api_key = config("ABSTRACTAPIKEY")
        #url = f"https://ipgeolocation.abstractapi.com/v1/?api_key={api_key}"
        url = "https://ipgeolocation.abstractapi.com/v1/?api_key=d77f75a5593e4073a6eb1bef9c35e929"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            user_geo_data, created = UserGeoData.objects.get_or_create(user=instance)
            user_geo_data.ip_address = data.get("ip_address")
            user_geo_data.city = data.get("city")
            user_geo_data.region_iso_code = data.get("region_iso_code")
            user_geo_data.country_code = data.get("country_code")
            user_geo_data.longitude = data.get("longitude")
            user_geo_data.latitude = data.get("latitude")
            user_geo_data.save()
            print("User created successfully")
        else:
            print("Failed to fetch IP data from the API")
            print("API Response Status Code:", response.status_code)
            print("API Response Content:", response.content)
 

