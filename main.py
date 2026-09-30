from event_module import add_event, list_events
from booking_module import book_event, cancel_booking
from report_module import rate_report, popular_event

# Menu
def main():
    while True:
        print("\nCAMPUS EVENT TRACKER")
        print("1. Add event")
        print("2. List events")
        print("3. Book an event")
        print("4. Cancel a booking")
        print("5. Fill-rate report")
        print("6. Most popular event")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Event title: ")
            venue = input("Venue: ")
            capacity = int(input("Capacity: "))
            add_event(title, venue, capacity)
        elif choice == "2":
            list_events()
        elif choice == "3":
            name = input("Your name: ")
            event_id = int(input("Event ID: "))
            book_event(name, event_id)
        elif choice == "4":
            booking_id = int(input("Booking ID: "))
            cancel_booking(booking_id)
        elif choice == "5":
            rate_report()
        elif choice == "6":
            popular_event()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()
