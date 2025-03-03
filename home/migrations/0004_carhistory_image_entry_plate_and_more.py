# Generated by Django 4.2.17 on 2025-03-02 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_alter_carhistory_created_date_alter_carhistory_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="carhistory",
            name="image_entry_plate",
            field=models.ImageField(
                blank=True, null=True, upload_to="images_entry_plates/"
            ),
        ),
        migrations.AddField(
            model_name="carhistory",
            name="image_entry_vehicle",
            field=models.ImageField(
                blank=True, null=True, upload_to="images_entry_vehicles/"
            ),
        ),
        migrations.AddField(
            model_name="carhistory",
            name="image_exit_plate",
            field=models.ImageField(
                blank=True, null=True, upload_to="images_exit_plates/"
            ),
        ),
        migrations.AddField(
            model_name="carhistory",
            name="image_exit_vehicle",
            field=models.ImageField(
                blank=True, null=True, upload_to="images_exit_vehicles"
            ),
        ),
        migrations.AlterField(
            model_name="carhistory",
            name="created_date",
            field=models.DateTimeField(
                verbose_name=datetime.datetime(
                    2025, 3, 2, 20, 1, 52, 185444, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
