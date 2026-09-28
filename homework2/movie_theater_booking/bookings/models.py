from django.db import models

# Create your models here.

class Movie(models.Models):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField():

class Seat:
     seat_number = models.PositiveIntegerField():
     booking_status = models.CharField(max_length=100)

class Booking:
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    booking_date = models.DateField()

        
