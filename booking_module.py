from models import Booking
from event_module import events, find_event

#Database- bookings list
bookings = []

#Module 2: Booking & Registration
def book_event(name, event_id):
    event = find_event(event_id)
    if event is None:
        print("Event not found.")
    elif event.has_space() == False:
        print("Sorry, this event is full!")
    else:
        new_id = len(bookings) + 1
        new_booking = Booking(new_id, name, event_id)
        bookings.append(new_booking)
        event.booked = event.booked + 1
        print("Booking successful! Your booking ID is", new_id)
def cancel_booking(booking_id):
    remove = None
    for booking in bookings:
        if booking.id == booking_id:
            remove = booking
    if remove is None:
        print("Booking not found.")
    else:
        bookings.remove(remove)
        event = find_event(remove.event_id)
        if event is not None:
            event.booked = event.booked - 1
        print("Booking cancelled.")
