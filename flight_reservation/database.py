import sqlite3
import pandas as pd

def create_tables():
    conn = sqlite3.connect('flight_reservation.db')
    cur = conn.cursor()

    # Customers Table
    cur.execute('''CREATE TABLE IF NOT EXISTS customers (
        cust_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT
    )''')

    # Bookings Table
    cur.execute('''CREATE TABLE IF NOT EXISTS bookings (
        booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
        cust_id INTEGER,
        flight_id INTEGER,
        seats_booked INTEGER,
        total_amount REAL,
        FOREIGN KEY (cust_id) REFERENCES customers(cust_id),
        FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
    )''')

    conn.commit()
    conn.close()
    print("✅ Database tables created successfully.")


def load_flight_data(csv_file):
    df = pd.read_csv(csv_file)

    conn = sqlite3.connect('flight_reservation.db')

    # Replace flights table with CSV data (includes all columns)
    df.to_sql('flights', conn, if_exists='replace', index=False)

    conn.close()
    print("✅ Flight data loaded into database successfully.")
