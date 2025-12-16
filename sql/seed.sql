-- Insert cities
INSERT INTO city (name) VALUES ('Delhi');
INSERT INTO city (name) VALUES ('Mumbai');

-- Insert sensor readings
INSERT INTO sensor_reading (city_id, timestamp)
VALUES
(1, '2024-01-01 10:00:00'),
(2, '2024-01-01 10:05:00');

-- Insert measurements
INSERT INTO measurement (
    reading_id, temperature, humidity, light, air_quality, sound, dust
)
VALUES
(1, 25.5, 60.2, 300.0, 120.5, 55.0, 40.0),
(2, 27.1, 58.0, 280.0, 110.2, 52.0, 38.0);
