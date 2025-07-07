import mysql.connector
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Connect to MySQL DB (update credentials as needed)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="flight_db"
)
cursor = conn.cursor()

# Generate and insert 20 fake bookings
for _ in range(20):
    passenger_name = fake.name()
    flight_number = f"AI{random.randint(100, 999)}"
    booking_date = fake.date_between(start_date='-30d', end_date='today')
    travel_date = booking_date + timedelta(days=random.randint(1, 30))
    source = fake.city()
    destination = fake.city()
    price = round(random.uniform(3000, 15000), 2)

    query = """
    INSERT INTO bookings (passenger_name, flight_number, booking_date, travel_date, source, destination, price)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (passenger_name, flight_number, booking_date, travel_date, source, destination, price)
    cursor.execute(query, values)

conn.commit()
cursor.close()
conn.close()

print("\nMock data inserted successfully.")
