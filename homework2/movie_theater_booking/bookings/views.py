from django.shortcuts import render, get_object_or_404
from .models import Movie, Seat, Booking
from rest_framework import permissions, viewsets, serializers
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [permissions.IsAuthenticated] 

    @action(detail=False, methods=['get'])
    def availability(self, request):
        seat_objects = Seat.objects.filter(booking_status = False)
        serialize_the_objects = self.get_serializer(seat_objects, many=True)
        return Response(serialize_the_objects.data)  

class BookingViewSet(viewsets.ModelViewSet):

    queryset = Booking.objects.all() #gets all records for this model
    serializer_class = BookingSerializer #assigns serializer class to booking
    permission_classes = [permissions.IsAuthenticated] #handles whether users are logged in or not

    def get_queryset(self):

        return Booking.objects.filter(user=self.request.user) #returns the booking history of the logged in user
                                                              #not everyone' user history

    def perform_create(self, serializer):

        if serializer.validated_data["seat"].booking_status == False: #if the seat from the serializer is not taken
            booking_object = serializer.save(user=self.request.user)  #then sets the booked seat to the user that made the request
            booking_object.seat.booking_status = True                 #Set booking status of that seat to True, meaning its taken now
            booking_object.seat.save()                                #save it in the database
        else:                                                         #else, that means the seat was already taken from someone else and raise error
           raise serializers.ValidationError('This seat is already booked. Choose a different seat.')
            
def movie_view(request):
    context = {
        "movies": Movie.objects.all()
    }
    return render(request, "bookings/movie_list.html", context)

def booking_view(request, movie_id):
    context = {
        "seats": Seat.objects.all(), 
        "movie": (get_object_or_404(Movie, id=movie_id))
    }
    return render(request, "bookings/seat_booking.html", context)
