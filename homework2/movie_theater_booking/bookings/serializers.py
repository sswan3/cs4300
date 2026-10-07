from .models import Movie, Seat, Booking
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id","title", "release_date", "description", "duration"]

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ["id","seat_number", "booking_status"]
        read_only_fields = ['booking_status'] 


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id","movie", "seat","user","booking_date"]
        read_only_fields = ['user']

        

