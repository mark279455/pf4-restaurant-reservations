from django.views.generic import CreateView
from django.contrib import messages
from .models import Reservation, Table
from .forms import ReservationForm


class AddReservationView(CreateView):
    """ add Reservation """
    template_name = 'reservations/add_reservation.html'
    model = Reservation
    form_class = ReservationForm
    success_url = 'reservations/reservationadmin'

    def form_valid(self, form):
        """
        Before form submission, assign table with lowest capacity
        needed for booking guests
        """
        form.instance.customer = self.request.user
        date = form.cleaned_data['reservation_date']
        time = form.cleaned_data['reservation_time']
        guests = form.cleaned_data['num_guests']
        # Filter tables with capacity greater or equal
        # to the number of guests
        tables_big_enough = list(Table.objects.filter(
            table_seats__gte=guests
        ))
        # Get bookings on specified date
        reservation_on_requested_date = Reservation.objects.filter(
            reservation_date=date, reservation_time=time)
        # Iterate over bookings to get tables not booked
        for reservation in reservation_on_requested_date:
            for table in tables_big_enough:
                if table.table_num == reservation.table.table_num:
                    tables_big_enough.remove(table)
                    break
        # Iterate over tables not booked to get lowest
        # capacity table to assign to booking
        lowest_capacity_table = tables_big_enough[0]
        for table in tables_big_enough:
            if table.capacity < lowest_capacity_table.capacity:
                lowest_capacity_table = table
        form.instance.table = lowest_capacity_table

        messages.success(
            self.request,
            f'Booking confirmed for {guests} guests on {date}'
        )

        return super(AddReservationView, self).form_valid(form)
