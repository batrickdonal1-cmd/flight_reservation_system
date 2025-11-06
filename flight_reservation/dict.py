# Flight Reservation System (No SQL, No Pandas)
# Data stored in Python dictionaries

flights = [
    {"flight_id": 101, "airline": "Air India", "source": "Bangalore", "destination": "Delhi", "price": 5000},
    {"flight_id": 102, "airline": "IndiGo", "source": "Bangalore", "destination": "Mumbai", "price": 4000},
    {"flight_id": 103, "airline": "SpiceJet", "source": "Chennai", "destination": "Delhi", "price": 4500},
    {"flight_id": 104, "airline": "Vistara", "source": "Delhi", "destination": "Kolkata", "price": 5500}
]

bookings = []


def view_flights():
    print("\nAvailable Flights:")
    print("{:<10} {:<15} {:<15} {:<15} {:<10}".format("ID", "Airline", "Source", "Destination", "Price"))
    for f in

    :
        print("{:<10} {:<15} {:<15} {:<15} ₹{:<10}".format(f["flight_id"], f["airline"], f["source"], f["destination"], f["price"]))


def search_flight(source, destination):
    print(f"\nFlights from {source} to {destination}:")
    found = False
    for f in flights:
        if f["source"].lower() == source.lower() and f["destination"].lower() == destination.lower():
            print(f"Flight ID: {f['flight_id']} | Airline: {f['airline']} | Price: ₹{f['price']}")
            found = True
    if not found:
        print("No flights found for your search.")


def book_ticket():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")

    try:
        flight_id = int(input("Enter Flight ID to book: "))
        seats = int(input("Enter number of seats: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    flight = next((f for f in flights if f["flight_id"] == flight_id), None)

    if flight:
        total = flight["price"] * seats
        booking = {
            "name": name,
            "email": email,
            "phone": phone,
            "flight_id": flight_id,
            "seats": seats,
            "total_amount": total
        }
        bookings.append(booking)
        print(f"\n✅ Booking confirmed for {name}! Total amount: ₹{total}")
    else:
        print("❌ Invalid Flight ID.")


def show_bookings():
    if not bookings:
        print("\nNo bookings yet.")
        return

    print("\nYour Bookings:")
    for b in bookings:
        print(f"Name: {b['name']}, Flight ID: {b['flight_id']}, Seats: {b['seats']}, Total: ₹{b['total_amount']}")


# Main menu
while True:
    print("\n---- FLIGHT RESERVATION SYSTEM ----")
    print("1. View Flights")
    print("2. Search Flight")
    print("3. Book Ticket")
    print("4. View My Bookings")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        view_flights()
    elif choice == '2':
        src = input("Enter source: ")
        dest = input("Enter destination: ")
        search_flight(src, dest)
    elif choice == '3':
        book_ticket()
    elif choice == '4':
        show_bookings()
    elif choice == '5':
        print("Thank you for using the Flight Reservation System!")
        break
    else:
        print("Invalid choice. Please try again.")
