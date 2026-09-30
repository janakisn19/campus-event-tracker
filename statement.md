# Problem Statement

College campuses run many events (workshops, fests, sports meets) but
students often have no easy way to see what's happening, check whether
seats are available, or reserve a spot before an event fills up. Organizers
similarly lack a simple way to track how many people have registered for
their event.

## Scope of the Project
This project is a command-line Python application that lets:
- Organizers add and list events with a venue and seat capacity
- Students book a seat at an event, with the system blocking bookings
  once an event reaches capacity
- Either role view simple analytics: fill-rate per event and the most
  popular event by booking count

The scope is intentionally limited to a single-session CLI tool (no
persistent database, no authentication, no GUI) to keep the project
focused on applying core Python concepts cleanly.

## Target Users
- **Event organizers** (student clubs, college committees) who need a
  quick way to list an event and see how full it is
- **Students** who want to check what events are on and reserve a seat

## High-Level Features
1. Event Management — add and view events
2. Booking & Registration — book or cancel a seat, with capacity checks
3. Reporting & Analytics — fill-rate report and most popular event
