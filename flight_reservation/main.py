import sqlite3
from database import create_tables, load_flight_data

def view_flights():
    conn = sqlite3.connect('flight_reservation.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM flights LIMIT 10")
    flights = cur.fetchall()
    conn.close()
    for f in flights:
        print(f)

def search_flights(source, destination):
    conn = sqlite3.connect('flight_reservation.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM flights WHERE source=? AND destination=?", (source, destination))
    flights = cur.fetchall()
    conn.close()
    return flights

def book_ticket(name, email, phone, flight_id, seats):
    conn = sqlite3.connect('flight_reservation.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
    cust_id = cur.lastrowid

    cur.execute("SELECT price FROM flights WHERE rowid=?", (flight_id,))  # changed to rowid
    result = cur.fetchone()
    if result:
        price = result[0]
        total = price * seats
        cur.execute("INSERT INTO bookings (cust_id, flight_id, seats_booked, total_amount) VALUES (?, ?, ?, ?)",
                    (cust_id, flight_id, seats, total))
        conn.commit()
        print(f"✅ Booking successful! Total amount = ₹{total}")
    else:
        print("❌ Invalid flight ID.")
    conn.close()

if __name__ == "__main__":
    create_tables()
    # Run only once to load CSV into database, then comment it out again
    load_flight_data(r"C:\Users\HP\Desktop\flight_reservation\flight_data.csv")

    print("---- FLIGHT RESERVATION SYSTEM ----")
    while True:
        print("\n1. View Flights\n2. Search Flight\n3. Book Ticket\n4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            view_flights()
        elif choice == '2':
            src = input("Enter source: ")
            dest = input("Enter destination: ")
            flights = search_flights(src, dest)
            if flights:
                for i, f in enumerate(flights, 1):
                    print(f"{i}. {f}")
            else:
                print("❌ No flights found.")
        elif choice == '3':
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            fid = int(input("Flight ID (row number from above list): "))
            seats = int(input("Seats: "))
            book_ticket(name, email, phone, fid, seats)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")
