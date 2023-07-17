# Generated by Django 4.2.3 on 2023-07-17 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Table",
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
                ("table_num", models.IntegerField(unique=True)),
                (
                    "table_seats",
                    models.IntegerField(
                        choices=[
                            (2, "2"),
                            (4, "4"),
                            (6, "6"),
                            (8, "8"),
                            (10, "10"),
                            (12, "12"),
                        ],
                        default=2,
                    ),
                ),
            ],
            options={
                "ordering": ["table_num"],
            },
        ),
        migrations.CreateModel(
            name="Reservation",
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
                ("cust_name", models.CharField(max_length=50)),
                ("num_guests", models.IntegerField(default=2)),
                ("reservation_date", models.DateField()),
                (
                    "reservation_time",
                    models.IntegerField(
                        choices=[
                            (1, "11:00 - 13:00"),
                            (2, "13:00 - 15:00"),
                            (3, "15:00 - 17:00"),
                            (4, "17:00 - 19:00"),
                            (5, "19:00 - 21:00"),
                            (6, "21:00 - 23:00"),
                        ],
                        default=1,
                    ),
                ),
                ("reservation_made_time", models.DateTimeField(auto_now_add=True)),
                ("notes", models.CharField(max_length=500)),
                (
                    "cust",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reservation_cust",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "table",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reserved_table",
                        to="reservations.table",
                    ),
                ),
            ],
            options={
                "ordering": ["reservation_date", "reservation_time", "cust_name"],
            },
        ),
    ]
