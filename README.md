# Campus Event Tracker & Booking System

A command-line Python application that lets a college manage campus events
and student bookings — built to apply core Python concepts (OOP, functions,
lists, dictionaries, loops, and decision-making) to a real-world problem.

## Overview
Students often miss out on campus events or double-book themselves because
there's no simple way to track event capacity and registrations. This
project provides a lightweight, no-database CLI tool where organizers can
list events and students can book a seat — with automatic capacity checks.

## Features
- Add and list campus events (title, venue, capacity)
- Book a seat at an event (blocks booking once an event is full)
- Cancel an existing booking
- View a fill-rate report (% of capacity booked) for every event
- Identify the most popular event by booking count

## Technologies / Tools Used
- Python 3 (standard library only — no external packages required)
- Object-Oriented Programming (`Event` and `Booking` classes)
- Git & GitHub for version control

## Project Structure
```
campus-event-tracker/
├── models.py          # Event and Booking classes
├── event_module.py    # Module 1: Event Management
├── booking_module.py  # Module 2: Booking & Registration
├── report_module.py   # Module 3: Reporting & Analytics
├── main.py             # CLI menu that ties the modules together
├── README.md
└── statement.md
```

## Setup & Installation
1. Install Python 3.10 or later from [python.org](https://python.org) if
   not already installed.
2. Clone this repository:
   ```
   git clone https://github.com/YOUR-USERNAME/campus-event-tracker.git
   cd campus-event-tracker
   ```
3. No external dependencies — nothing to install via pip.

## How to Run
From the project's root folder, run:
```
python main.py
```
You'll see a menu. Enter the number for the action you want (add event,
book event, etc.) and follow the prompts.

## How to Test
There's no separate automated test suite; test manually by:
1. Choosing option 1 to add an event with a small capacity (e.g. 2).
2. Choosing option 3 to book it with 2-3 different names.
3. Confirming the 3rd booking is rejected once capacity is reached.
4. Choosing option 5 to confirm the fill-rate report shows 100%.

## Screenshots
*(Add a screenshot of the menu and a sample run here before submitting.)*

## Future Enhancements
- Persist data to a file so events/bookings survive between runs
- Add a waitlist instead of flatly rejecting bookings once full
- Build a simple web interface on top of the same modules
