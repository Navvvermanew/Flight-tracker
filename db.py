import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*******", # Will write my password when use
    database="flight_app"
)
cursor = conn.cursor(dictionary=True)

def get_flights():
    cursor.execute("SELECT * FROM flights;")
    return cursor.fetchall()

def get_delays():
    cursor.execute("""
        SELECT f.flight_id, f.airline, fd.delay_minutes, fd.delay_reason, fd.logged_on
        FROM flight_delays fd
        JOIN flights f ON fd.flight_id = f.flight_id
        ORDER BY fd.logged_on DESC;
    """)
    return cursor.fetchall()
