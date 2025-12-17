-- 1. Total number of charted holiday songs
SELECT COUNT(*) FROM holiday_songs;

-- 2. Top 10 songs with best average chart position
SELECT
    song_title,
    artist,
    ROUND(AVG(chart_position), 2) AS avg_position
FROM holiday_songs
GROUP BY song_title, artist
ORDER BY avg_position ASC
LIMIT 10;

-- 3. Number of charted songs per year
SELECT
    year,
    COUNT(*) AS total_songs
FROM holiday_songs
GROUP BY year
ORDER BY year;

-- 4. Query performance check (uses index on year)
EXPLAIN ANALYZE
SELECT *
FROM holiday_songs
WHERE year = 2011;



-- ================================
-- Earthquake Dataset Queries
-- ================================

-- 1. Total earthquakes loaded
SELECT COUNT(*) FROM earthquakes;

-- 2. Average magnitude per decade
SELECT
    (EXTRACT(YEAR FROM quake_date)::INT / 10) * 10 AS decade,
    ROUND(AVG(magnitude)::NUMERIC, 2) AS avg_magnitude,
    COUNT(*) AS quake_count
FROM earthquakes
GROUP BY decade
ORDER BY decade

-- 3. Deepest earthquakes
SELECT
    quake_date,
    depth_km,
    magnitude
FROM earthquakes
ORDER BY depth_km DESC
LIMIT 10;

-- 4. Performance test (before/after index)
EXPLAIN ANALYZE
SELECT *
FROM earthquakes
WHERE magnitude >= 7.5;
