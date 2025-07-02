CREATE DATABASE IF NOT EXISTS flight_app;
USE flight_app;

CREATE TABLE IF NOT EXISTS passengers (
    passenger_id VARCHAR(10) PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS flights (
    flight_id VARCHAR(10) PRIMARY KEY,
    airline VARCHAR(50),
    departure_airport VARCHAR(50),
    arrival_airport VARCHAR(50),
    scheduled_departure DATETIME,
    scheduled_arrival DATETIME
);

CREATE TABLE IF NOT EXISTS bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    passenger_id VARCHAR(10),
    flight_id VARCHAR(10),
    booking_date DATE,
    seat_number VARCHAR(5),
    FOREIGN KEY (passenger_id) REFERENCES passengers(passenger_id),
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
);

CREATE TABLE IF NOT EXISTS flight_delays (
    delay_id INT AUTO_INCREMENT PRIMARY KEY,
    flight_id VARCHAR(10),
    delay_reason VARCHAR(100),
    delay_minutes INT,
    logged_on DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
);
