import uuid
import requests
from .api import fetch_user_geo_data, extract_user_geo_data

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager




class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(verbose_name=_("Username"), max_length=255, unique=True)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=50)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=50)
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def _str_(self):
        return self.username

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.username
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.id:
            api_response = fetch_user_geo_data(self.id)
            user_geo_data = extract_user_geo_data(api_response)
            try:
                user_geo = UserGeoData(user=self, **user_geo_data)
                user_geo.save()
            except Exception as e:
                print(f"Error creating UserGeoData: {e}")
    
    
    
class UserGeoData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    ip_address = models.GenericIPAddressField(default="0.0.0.0")
    city = models.CharField(max_length=50)
    region_iso_code = models.CharField(max_length=5)
    country_code = models.CharField(max_length=5)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    security = models.BooleanField(default=False)
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     if not self.usergeo:
    #         api_response = fetch_user_geo_data(self.id)
    #         user_geo_data = extract_user_geo_data(api_response)
    #         try:
    #             user_geo = UserGeoData(user=self, **user_geo_data)
    #             user_geo.save()
    #         except Exception as e:
    #             print(f"Error creating UserGeoData: {e}")



    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     api_response = fetch_user_geo_data(self.id)
    #     user_geo_data = extract_user_geo_data(api_response)
    #     user_geo = UserGeoData(user=self, **user_geo_data)
    #     user_geo.save()
        

# class Holiday(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     holiday_name = models.CharField(max_length=120)
#     holiday_type = models.CharField(max_length=120)
#     date = models.DateTimeField(auto_now=True)
