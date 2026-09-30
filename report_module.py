from event_module import events

#Module 3: Reports
def rate_report():
    if len(events) == 0:
        print("No events yet.")
    else:
        for event in events:
            if event.capacity > 0:
                rate = (event.booked / event.capacity) * 100
            else:
                rate = 0
            print(event.title, "is", round(rate, 1), "% full")
def popular_event():
    if len(events) == 0:
        print("No events yet.")
        return
    top_event = events[0]  #start by assuming the first event is the most popular
    for event in events:
        if event.booked > top_event.booked:
            top_event = event
    print("Most popular event:", top_event.title, "with", top_event.booked, "bookings")
