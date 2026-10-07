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

    def get_queryset(self):

        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):

        if get_queryset().seat.booking_status == False:
            booking_object = serializer.save(user=self.request.user)
            booking_object.seat.booking_status = True
            booking_object.seat.save()
        else:
           raise serializers.ValidationError('This seat is already booked. Choose a different seat.')
            



    


