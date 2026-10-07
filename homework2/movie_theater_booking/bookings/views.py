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
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        super().get_queryset(self.request.user) 
        booking_object = serializer.save(user=self.request.user)
        if booking_object.seat.booking_status = False:
            booking_object.seat.booking_status = True
            booking_object.seat.save()
        else:
            print("This seat is already booked")
            



    


