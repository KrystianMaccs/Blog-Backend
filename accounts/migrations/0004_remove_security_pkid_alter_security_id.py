# Generated by Django 4.2.6 on 2023-10-15 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_remove_usergeodata_pkid_alter_usergeodata_id_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="security",
            name="pkid",
        ),
        migrations.AlterField(
            model_name="security",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
