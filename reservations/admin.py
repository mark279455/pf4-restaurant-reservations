from django.contrib import admin
from .models import (Table, Reservation)


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = (
        "table_num",
        "table_seats"
    )
    list_filter = ( "table_seats", )

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "reservation_made_time",
        "cust_name",
        "table",
        "num_guests",
        "reservation_date",
        "reservation_time",
        "notes"
    )
    list_filter = ("reservation_date", "reservation_time" )

