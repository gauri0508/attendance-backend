-- Task 7: Holiday Songs Dataset (Actual Columns)

DROP TABLE IF EXISTS holiday_songs;

CREATE TABLE holiday_songs (
    song_id SERIAL PRIMARY KEY,
    song_title TEXT NOT NULL,
    artist TEXT NOT NULL,
    year INT NOT NULL,
    chart_position INT,
    chart_date DATE
);

-- Indexes for analytical queries
CREATE INDEX idx_holiday_year ON holiday_songs(year);
CREATE INDEX idx_chart_date ON holiday_songs(chart_date);



-- ================================
-- Task 7: Earthquake Dataset
-- ================================

DROP TABLE IF EXISTS earthquakes;

CREATE TABLE earthquakes (
    quake_id SERIAL PRIMARY KEY,
    quake_date DATE NOT NULL,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    depth_km DOUBLE PRECISION,
    magnitude DOUBLE PRECISION
);

-- Indexes for optimization
CREATE INDEX idx_quake_date ON earthquakes(quake_date);
CREATE INDEX idx_quake_magnitude ON earthquakes(magnitude);
