# Generated by Django 4.2.3 on 2023-07-17 14:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("reservations", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="reservation",
            options={"ordering": ["reservation_date", "reservation_time"]},
        ),
    ]
