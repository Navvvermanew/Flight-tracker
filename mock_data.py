import mysql.connector
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",  # change this
    database="flight_app"
)
cursor = conn.cursor()

# Populating passengers table
passenger_ids = []
for _ in range(10):
    passenger_id = fake.unique.bothify(text='P####')
    full_name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    passenger_ids.append(passenger_id)
    
    cursor.execute("""
        INSERT INTO passengers (passenger_id, full_name, email, phone)
        VALUES (%s, %s, %s, %s)
    """, (passenger_id, full_name, email, phone))

# Populating flights table
flight_ids = []
for _ in range(5):
    flight_id = fake.unique.bothify(text='F###')
    airline = fake.company()
    departure_airport = fake.city()
    arrival_airport = fake.city()
    scheduled_departure = fake.date_time_between(start_date="+1d", end_date="+5d")
    scheduled_arrival = scheduled_departure + timedelta(hours=random.randint(1, 5))
    flight_ids.append(flight_id)

    cursor.execute("""
        INSERT INTO flights (flight_id, airline, departure_airport, arrival_airport, scheduled_departure, scheduled_arrival)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (flight_id, airline, departure_airport, arrival_airport, scheduled_departure, scheduled_arrival))

# Populating bookings table
for _ in range(20):
    passenger_id = random.choice(passenger_ids)
    flight_id = random.choice(flight_ids)
    booking_date = fake.date_between(start_date="-30d", end_date="today")
    seat_number = f"{random.randint(1, 30)}{random.choice(['A', 'B', 'C', 'D'])}"

    cursor.execute("""
        INSERT INTO bookings (passenger_id, flight_id, booking_date, seat_number)
        VALUES (%s, %s, %s, %s)
    """, (passenger_id, flight_id, booking_date, seat_number))

# Populating flight_delays table
for _ in range(10):
    flight_id = random.choice(flight_ids)
    delay_reason = random.choice([
        "Technical Issue", "Bad Weather", "ATC Delay", "Late Arrival", "Security Clearance"
    ])
    delay_minutes = random.randint(10, 180)

    cursor.execute("""
        INSERT INTO flight_delays (flight_id, delay_reason, delay_minutes)
        VALUES (%s, %s, %s)
    """, (flight_id, delay_reason, delay_minutes))

# Commit and close
conn.commit()
cursor.close()
conn.close()

print("\nMock data inserted successfully.")

