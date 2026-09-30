from models import Event

#Database- events list
events = []

#Module 1: Event Management
def add_event(title, venue, capacity):
    new_id = len(events) + 1  #simple way to make each ID unique
    new_event = Event(new_id, title, venue, capacity)
    events.append(new_event)
    print("Event added successfully!")
def list_events():
    if len(events) == 0:
        print("No events yet.")
    else:
        for event in events:
            event.display()
def find_event(event_id):
    #Loop through the list and return the matching event
    for event in events:
        if event.id == event_id:
            return event
    return None  #Event not found
