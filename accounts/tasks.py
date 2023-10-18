# from celery import shared_task
# from .models import User, UserGeoData
# import requests

# @shared_task
# def populate_user_geo_data(id):
#     user = User.objects.get(id=id)
#     geolocation_data = requests.get('https://ipgeolocation.abstractapi.com/v1/?api_key=d77f75a5593e4073a6eb1bef9c35e929')
    
#     ip_address = geolocation_data['ip_address']
#     city = geolocation_data['city']
#     region_iso_code = geolocation_data['region_iso_code']
#     country_code = geolocation_data['country_code']
#     longitude = geolocation_data['longitude']
#     latitude = geolocation_data['latitude']

#     # Create UserGeoData object and save it
#     user_geo_data = UserGeoData(
#         user=user,
#         ip_address=ip_address,
#         city=city,
#         region_iso_code=region_iso_code,
#         country_code=country_code,
#         longitude=longitude,
#         latitude=latitude
#     )
#     user_geo_data.save()

# # @shared_task
# # def check_for_holiday(id):
# #     user = User.objects.get(id=id)
# #     holiday_data = requests.get('("https://holidays.abstractapi.com/v1/?api_key=9cb9967be3054f95a7f4c80fae708370&country={country_code}&year=2020&month=12&day=25")', params={'country_code': user.usergeo.country_code, 'date': user.date_joined})

# #     if holiday_data['is_holiday']:
# #         holiday_name = holiday_data['holiday_name']
# #         holiday_type = holiday_data['holiday_type']
# #         holiday = Holiday(
# #             user=user,
# #             holiday_name=holiday_name,
# #             holiday_type=holiday_type
# #         )
# #         holiday.save()
