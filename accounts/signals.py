import requests
from decouple import config
from .models import User, UserGeoData



@receiver(post_save, sender=User)
def update_location(sender, instance, created, **kwargs):
    if created:
        api_key = config("ABSTRACTAPIKEY")
        url = f"https://ipgeolocation.abstractapi.com/v1/?api_key={api_key}"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            location = UserGeoData(
                ip_address=data['ip_address'],
                city=data['city'],
                region_iso_code=data['region_iso_code'],
                country=data['country'],
                longitude=data['longitude'],
                latitude=data['latitude']
            )
            location.save()
