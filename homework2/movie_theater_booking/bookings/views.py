from django.shortcuts import render
from .models import Movie, Seat, Booking
from rest_framework import permissions, viewsets
from movie_theater_booking.bookings.serializers import MovieSerializer, SeatSerializer, BookingSerializer


# Create your views here.


