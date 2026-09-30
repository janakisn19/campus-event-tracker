#Classes
class Event:
    def __init__(self, event_id, title, venue, capacity):
        self.id = event_id
        self.title = title
        self.venue = venue
        self.capacity = capacity
        self.booked = 0  #nobody has booked yet
    def has_space(self):
        #True if seats are still available
        return self.booked < self.capacity
    def display(self):
        print(self.id, "(Event ID):", self.title, "@", self.venue, "-", self.booked, "/", self.capacity, "booked")
class Booking:
    def __init__(self, booking_id, name, event_id):
        self.id = booking_id
        self.name = name
        self.event_id = event_id
