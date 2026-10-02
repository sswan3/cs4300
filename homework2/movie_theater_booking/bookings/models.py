from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Seat(models.Model):
     seat_number = models.PositiveIntegerField():
     booking_status = models.CharField(max_length=100)

     def __str__(self):
        return f"Seat {self.seat_number}"

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    booking_date = models.DateField()

    def __str__(self):
        return f"{self.user} - {self.movie} - {self.seat}"

        
