import requests
from decouple import config
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserGeoData

from blog.settings.base import AUTH_USER_MODEL


@receiver(post_save, sender=AUTH_USER_MODEL)
def fetch_and_save_ip_and_country(sender, instance, created, **kwargs):
    if created:
        api_key = config("ABSTRACTAPIKEY")
        url = f"https://ipgeolocation.abstractapi.com/v1/?api_key={api_key}"
        response = requests.get(api_url)

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
        else:
            print("Failed to fetch IP data from the API")

