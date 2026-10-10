from django.test import TestCase
from .models import Movie, Seat, Booking
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from datetime import date
from rest_framework.test import APITestCase
from rest_framework import status

class BookingViewSetTestCase(APITestCase):
    def setUp(self):
        # Saved to self.* so test methods can access them
        self.movie = Movie.objects.create(
            title="My Little Pony",
            description="friendship and love is learned",
            release_date="2026-11-14",
            duration=2
        )
        self.seat = Seat.objects.create(seat_number=77, booking_status=False)
        self.user = User.objects.create_user(username="lauren", password="testpass123")
    def test_not_loggedin_book_seat(self):
        self.client.force_authenticate(user=None)
        payload = {
            "movie": self.movie.id,
            "seat": self.seat.id,
            "booking_date": str(date.today())
        }

        response = self.client.post('/api/bookings/', payload, format='json')

        self.assertEqual response.status_code == status.HTTP_401, status.HTTP_403
        self.assertEqual(Booking.objects.count(), 1)

    def test_login_book_seat(self):
        # Authenticate the pre-built test client
        self.client.force_authenticate(user=self.user)

        # Send Primary Key IDs for ForeignKeys and ISO string for date
        payload = {
            "movie": self.movie.id,
            "seat": self.seat.id,
            "booking_date": str(date.today())
        }

        response = self.client.post('/api/bookings/', payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)
        self.seat.refresh_from_db()
        self.assertEqual(self.seat.booking_status, True)

class MovieTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(title="My Little Pony", description="friendship and love is learned"
        ,release_date = "2026-11-14", duration=2)

    def test_movie_storage(self):
        movie = Movie.objects.get(title="My Little Pony")
        self.assertEqual(movie.title, "My Little Pony")
        self.assertEqual(movie.description, "friendship and love is learned")
        self.assertEqual(str(movie.release_date), "2026-11-14")
        self.assertEqual(movie.duration, 2)

class IncorrectMovieTestCase(TestCase):

    def test_values(self):

        with self.assertRaises(ValueError):
            Movie.objects.create(title="My Little Pony", description="friendship and love is learned"
            ,release_date = "2026-11-14", duration="not_a_number")
            #self.assertIsInstance(movie.duration, int) 


class SeatTestCase(TestCase):
    def setUp(self):
        Seat.objects.create(seat_number = 76, booking_status = False)

    def test_seat_storage(self):
        seat = Seat.objects.get(seat_number = 76)
        self.assertEqual(seat.seat_number, 76)
        self.assertEqual(seat.booking_status, False)

class BookTestCase(TestCase):
    def setUp(self):
        movie = Movie.objects.create(
            title="Avengers", 
            description="fighting and blood occurs", 
            release_date="2026-12-25", 
            duration=3
        )
        seat = Seat.objects.create(seat_number=77, booking_status=False)
        user = self.user = User.objects.create_user(username="testuser", password="testpass123")
        booking_date = date.today()
        
        Booking.objects.create(
            movie=movie, 
            seat=seat, 
            user=user, 
            booking_date=booking_date
        )

    def test_booking_storage(self):
        today = date.today()
        book = Booking.objects.get(booking_date=today)
        self.assertEqual(book.movie.title, "Avengers")
        self.assertEqual(book.movie.description, "fighting and blood occurs")
        self.assertEqual(book.movie.duration, 3)
        self.assertEqual(book.movie.release_date, date(2026, 12, 25))
        self.assertEqual(book.seat.seat_number, 77)
        self.assertEqual(book.seat.booking_status, False)
        self.assertEqual(book.user.username, "testuser")
        self.assertEqual(book.booking_date, today)
        
        

        
