# Generated by Django 4.2.17 on 2025-03-02 18:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="carhistory",
            options={"verbose_name_plural": "Historial de accesos"},
        ),
        migrations.AlterField(
            model_name="carhistory",
            name="created_date",
            field=models.DateTimeField(
                verbose_name=datetime.datetime(
                    2025, 3, 2, 18, 22, 42, 109531, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="carhistory",
            name="entry_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="carhistory",
            name="exit_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
