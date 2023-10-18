import requests



def fetch_user_geo_data(user_id):
    response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=9cb9967be3054f95a7f4c80fae708370")
    if response.status_code == 200:
        return response.json()
        print("API responded successfully")
    else:
        raise Exception(f"Failed to fetch the User Geo data: {response.status_code}")
        print("API failed")
    
    
    
def extract_user_geo_data(api_response):
    user_geo_data = {
        "ip_address": api_response["ip_address"],
        "city = data": api_response["city"],
        "region_iso_code": api_response["region_iso_code"],
        "country_code": api_response["longitude"],
        "latitude": api_response["latitude"],
        "security": api_response["security"]["is_vpn"],
    }
    return user_geo_data