-- Drop tables if they exist (safe re-run)
DROP TABLE IF EXISTS measurement;
DROP TABLE IF EXISTS sensor_reading;
DROP TABLE IF EXISTS city;

-- =========================
-- City Table
-- =========================
CREATE TABLE city (
    city_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

-- =========================
-- Sensor Reading Table
-- =========================
CREATE TABLE sensor_reading (
    reading_id SERIAL PRIMARY KEY,
    city_id INT NOT NULL,
    timestamp TIMESTAMP NOT NULL,

    CONSTRAINT fk_city
        FOREIGN KEY (city_id)
        REFERENCES city(city_id)
        ON DELETE CASCADE,

    CONSTRAINT unique_city_timestamp
        UNIQUE (city_id, timestamp)
);

-- =========================
-- Measurement Table
-- =========================
CREATE TABLE measurement (
    measurement_id SERIAL PRIMARY KEY,
    reading_id INT NOT NULL,

    temperature FLOAT,
    humidity FLOAT,
    light FLOAT,
    air_quality FLOAT,
    sound FLOAT,
    dust FLOAT,

    CONSTRAINT fk_reading
        FOREIGN KEY (reading_id)
        REFERENCES sensor_reading(reading_id)
        ON DELETE CASCADE
);

-- =========================
-- Indexes for Performance
-- =========================
CREATE INDEX idx_sensor_city ON sensor_reading(city_id);
CREATE INDEX idx_sensor_timestamp ON sensor_reading(timestamp);
CREATE INDEX idx_measurement_reading ON measurement(reading_id);
