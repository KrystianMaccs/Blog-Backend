import requests
from celery import shared_task
from .models import UserGeoData, Security, Holiday
import datetime



GEO_API_URL = 'https://ipgeolocation.abstractapi.com/v1/?api_key=d77f75a5593e4073a6eb1bef9c35e929'
HOLIDAY_API_BASE_URL = 'https://holidays.abstractapi.com/v1/?api_key=9cb9967be3054f95a7f4c80fae708370'

@shared_task
def fetch_and_save_geodata():
    try:
        response = requests.get(GEO_API_URL)
        response.raise_for_status()

        data = response.json()
        
        ip_address = data['ip_address']
        city = data['city']
        region_iso_code = data['region_iso_code']
        country_code = data['country_code']
        longitude = data['longitude']
        latitude = data['latitude']
        is_vpn = data['security']['is_vpn']

        user_geo_data, created = UserGeoData.objects.update_or_create(
            ip_address=ip_address,
            defaults={
                'city': city,
                'region_iso_code': region_iso_code,
                'country_code': country_code,
                'longitude': longitude,
                'latitude': latitude,
            }
        )
        security, created = Security.objects.update_or_create(
            defaults={'is_vpn': is_vpn}
        )
        user_geo_data.security = security
        user_geo_data.save()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching geo data: {e}")



@shared_task
def fetch_and_save_holiday_data(id):
    try:
        user_geo_data = UserGeoData.objects.get(id=id)
        country_code = user_geo_data.country_code

        current_date = datetime.date.today()
        year = current_date.year
        month = current_date.month
        day = current_date.day

        holiday_api_url = f'{HOLIDAY_API_BASE_URL}&country={country_code}&year={year}&month={month}&day={day}'

        response = requests.get(holiday_api_url)
        response.raise_for_status()
        data = response.json()
        holiday_name = data['name']
        holiday_type = data['type']
        holiday, created = Holiday.objects.update_or_create(
            user=user_geo_data.user,
            defaults={
                'holiday_name': holiday_name,
                'holiday_type': holiday_type,
            }
        )
    except (UserGeoData.DoesNotExist, requests.exceptions.RequestException) as e:
        print(f"Error fetching holiday data: {e}")