from django.urls import path
from . import views

urlpatterns = [
    path('addreservation/', views.AddReservationView.as_view(),
         name='addreservation'
         )
]

# path(
#     'managebookings/',
#     views.BookingsList.as_view(),
#     name='managebookings'),
# path(
#     'editbooking/<slug:pk>/',
#     views.EditBookingView.as_view(),
#     name='editbooking'),
# path(
#     'delete/<slug:pk>/',
#     views.DeleteBookingView.as_view(),
#     name="delete_booking")
