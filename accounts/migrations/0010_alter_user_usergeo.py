# Generated by Django 4.2.6 on 2023-10-18 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_remove_security_usergeodata_usergeodata_security_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="usergeo",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.usergeodata",
            ),
        ),
    ]
