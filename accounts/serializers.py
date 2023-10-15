from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserGeoData

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
        
        

class UserGeoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGeoData
        fields = ('ip_address', 'city', 'region_iso_code', 'country_code', 'longitude', 'latitude')
