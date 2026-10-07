from django.shortcuts import render
from .models import Movie, Seat, Booking
from rest_framework import permissions, viewsets
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):

    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        booking_object = serializer.save(user=self.request.user)
        change_status = booking_object.seat.booking_status = True
        change_status.save()



    


