# Generated by Django 4.2.6 on 2023-10-16 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_alter_usergeodata_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usergeodata",
            name="user",
        ),
        migrations.AddField(
            model_name="user",
            name="usergeo",
            field=models.OneToOneField(
                default="User's Geolocation",
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.usergeodata",
            ),
        ),
    ]
