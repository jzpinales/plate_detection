# Generated by Django 5.1.4 on 2025-01-11 16:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CarHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("vehicle_plate", models.CharField(max_length=20)),
                ("vehicle_color", models.CharField(max_length=20)),
                (
                    "vehicle_type",
                    models.CharField(
                        choices=[
                            ("car", "Car"),
                            ("mot", "Motorcycle"),
                            ("bus", "Autobus"),
                            ("tru", "Truck"),
                            ("oth", "Other"),
                        ],
                        default="car",
                        max_length=3,
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(verbose_name=django.utils.timezone.now),
                ),
                ("entry_date", models.DateTimeField()),
                ("exit_date", models.DateTimeField()),
                ("price", models.FloatField()),
            ],
        ),
    ]
