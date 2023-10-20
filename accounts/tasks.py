import requests
from celery import shared_task
from .models import Holiday, UserGeoData, User
import datetime
import json



GEO_API_URL = 'https://ipgeolocation.abstractapi.com/v1/?api_key=d77f75a5593e4073a6eb1bef9c35e929'
HOLIDAY_API_BASE_URL = 'https://holidays.abstractapi.com/v1/?api_key=9cb9967be3054f95a7f4c80fae708370'


@shared_task
def fetch_and_save_geodata(user_id):
    user = User.objects.get(id=user_id)
    
    response = requests.get(GEO_API_URL)
    if response.status_code == 200:
        data = response.json()
        
        user_geo_data = UserGeoData(
            user=user,
            ip_address=data["ip_address"],
            city=data["city"],
            region_iso_code=data["region_iso_code"],
            country_code=data["country_code"],
            longitude=data["longitude"],
            latitude=data["latitude"],
        )
        user_geo_data.save()
    # try:
    #     response = requests.get(GEO_API_URL)
    #     data = response.json()
        
    #     ip_address = data['ip_address']
    #     city = data['city']
    #     region_iso_code = data['region_iso_code']
    #     country_code = data['country_code']
    #     longitude = data['longitude']
    #     latitude = data['latitude']

    #     user_geo_data, created = UserGeoData.objects.update_or_create(
    #         ip_address=ip_address,
    #         defaults={
    #             'city': city,
    #             'region_iso_code': region_iso_code,
    #             'country_code': country_code,
    #             'longitude': longitude,
    #             'latitude': latitude,
    #         }
    #     )
    #     user_geo_data.save()
    # except requests.exceptions.RequestException as e:
    #     print(f"Error fetching geo data: {e}")



# @shared_task
# def fetch_and_save_holiday_data(id):
#     try:
#         user_geo_data = UserGeoData.objects.get(id=id)
#         country_code = user_geo_data.country_code

#         current_date = datetime.date.today()
#         year = current_date.year
#         month = current_date.month
#         day = current_date.day

#         holiday_api_url = f'{HOLIDAY_API_BASE_URL}&country={country_code}&year={year}&month={month}&day={day}'

#         response = requests.get(holiday_api_url)
#         response.raise_for_status()
#         data = response.json()
#         holiday_name = data['name']
#         holiday_type = data['type']
#         holiday, created = Holiday.objects.update_or_create(
#             user=user_geo_data.user,
#             defaults={
#                 'holiday_name': holiday_name,
#                 'holiday_type': holiday_type,
#             }
#         )
#     except (UserGeoData.DoesNotExist, requests.exceptions.RequestException) as e:
#         print(f"Error fetching holiday data: {e}")

# @shared_task
# def fetch_and_save_holiday_data(id):
#     try:
#         user_geo_data = UserGeoData.objects.get(id=id)
#     except UserGeoData.DoesNotExist:
#         print(f"UserGeoData with id {id} does not exist.")
#         return
#     country_code = user_geo_data.country_code
#     current_date = datetime.date.today()
#     year = current_date.year
#     month = current_date.month
#     day = current_date.day
#     holiday_api_url = f'{HOLIDAY_API_BASE_URL}&country={country_code}&year={year}&month={month}&day={day}'
#     try:
#         response = requests.get(holiday_api_url)
#         response.raise_for_status()
#         data = response.json()
#         holiday_name = data['name']
#         holiday_type = data['type']
#         holiday, created = Holiday.objects.update_or_create(
#             user=user_geo_data.user,
#             defaults={
#                 'holiday_name': holiday_name,
#                 'holiday_type': holiday_type,
#             }
#         )
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching holiday data: {e}")
