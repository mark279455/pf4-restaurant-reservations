from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    """ form for new Reservation """
    class Meta:
        model = Reservation
        fields = [
            'cust_name', 'num_guests', 'reservation_date', 'reservation_time'
        ]
        booking_date = forms.DateField(help_text="Date must be in the future")
        labels = {
            'cust_name': 'Name',
            'num_guests': 'Number Of Guests',
            'reservation_date': 'Date',
            'reservation_time': 'Time',
        }
