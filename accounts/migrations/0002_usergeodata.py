# Generated by Django 4.2.6 on 2023-10-14 00:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserGeoData",
            fields=[
                (
                    "pkid",
                    models.BigIntegerField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("ip_address", models.GenericIPAddressField(default="0.0.0.0")),
                ("city", models.CharField(max_length=50)),
                ("region_iso_code", models.CharField(max_length=5)),
                ("country_code", models.CharField(max_length=5)),
                ("longitude", models.DecimalField(decimal_places=6, max_digits=9)),
                ("latitude", models.DecimalField(decimal_places=6, max_digits=9)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
