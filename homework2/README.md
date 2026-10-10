# Advanced Software Engineering HW2

## Setup
Go to this link: https://cs4300-n2ie.onrender.com
add /admin/ to the link in the browswer when you visit it or simply click any
button to get to the login page
login using admin and password = 123

## How to Navigate

-Click Home to go to the main selection that shows all the movies

-Click Book Now to book a certain movie

-Click a green seat to choose where you want to sit

-Click Dropdown -> Booking History to see past tickets you've booked. Including the one you made now!


## Running Tests

-navigate to movie_theater_booking directory

-run "python manage.py test" to go through all the tests

## Limitations

When you book a seat, it will turn gray, meaning its taken. 
However, it will do this for all movies. If you book Seat 1, 
it will be grayed out for movie 1 and movie 2 and all the 
movies in selection.

## Ai Use

Pardot and Gemini were used to debug. I often used them to help me
identify small syntax errors that are hard to spot, as well as explain
how Django and some of its functions work and any misunderstandings I 
was having with them. I used gemini to rewrite a
test_login_book_seat because I had trouble understanding how to implement
the payload to a request. I also used Gemini to write the booking_history_view 
in views.py. Other ways I used it, was helping me find resources
for understanding the material better, helping me 
navigate deployment, and explaining any random confusions I had about the 
linked documents in the HW pdf.




