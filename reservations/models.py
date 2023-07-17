from django.db import models
from django.contrib.auth.models import User

NUM_SEATS = (
    (2, '2'), (4, '4'),
    (6, '6'), (8, '8'),
    (10, '10'), (12, '12'),
)

RESERVATION_TIME_CHOICE = (
    (1, '11:00 - 13:00'), (2, '13:00 - 15:00'),
    (3, '15:00 - 17:00'), (4, '17:00 - 19:00'),
    (5, '19:00 - 21:00'), (6, '21:00 - 23:00')
)

class Table(models.Model):
    """ model for restaurant tables """
    table_num=models.IntegerField(unique=True)
    table_seats=models.IntegerField(choices=NUM_SEATS, default=2)

    class Meta:
        """ table_num """
        ordering = ['table_num' ]

    def __str__(self):
        return str(self.table_num)

class Reservation(models.Model):
    """ model for restaurant reservations """
    cust = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservation_cust")
    cust_name = models.CharField(max_length=50)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="reserved_table")
    num_guests = models.IntegerField(default=2)
    reservation_date = models.DateField()
    reservation_time = models.IntegerField(choices=RESERVATION_TIME_CHOICE, default=1)
    reservation_made_time = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=500)

    class Meta:
        """ date / time """
        ordering = ['reservation_date', 'reservation_time' ]

    def __str__(self):
        return str(self.pk)
