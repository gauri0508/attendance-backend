-- 1. Count total sensor readings per city
SELECT
    c.name AS city,
    COUNT(sr.reading_id) AS total_readings
FROM city c
JOIN sensor_reading sr ON c.city_id = sr.city_id
GROUP BY c.name
ORDER BY total_readings DESC;

-- 2. Average temperature per city
SELECT
    c.name AS city,
    ROUND(AVG(m.temperature), 2) AS avg_temperature
FROM city c
JOIN sensor_reading sr ON c.city_id = sr.city_id
JOIN measurement m ON sr.reading_id = m.reading_id
GROUP BY c.name;

-- 2. Average temperature per city
SELECT
    c.name AS city,
    ROUND(AVG(m.temperature), 2) AS avg_temperature
FROM city c
JOIN sensor_reading sr ON c.city_id = sr.city_id
JOIN measurement m ON sr.reading_id = m.reading_id
GROUP BY c.name;

-- 4. Maximum air quality reading per city
SELECT
    c.name AS city,
    MAX(m.air_quality) AS max_air_quality
FROM city c
JOIN sensor_reading sr ON c.city_id = sr.city_id
JOIN measurement m ON sr.reading_id = m.reading_id
GROUP BY c.name;

-- 5. Detect duplicate sensor readings (data issue detection)
SELECT
    city_id,
    timestamp,
    COUNT(*) AS occurrences
FROM sensor_reading
GROUP BY city_id, timestamp
HAVING COUNT(*) > 1;

-- 6. Find readings with missing sensor values
SELECT
    sr.reading_id,
    c.name AS city,
    sr.timestamp
FROM sensor_reading sr
JOIN city c ON sr.city_id = c.city_id
JOIN measurement m ON sr.reading_id = m.reading_id
WHERE
    m.temperature IS NULL
    OR m.humidity IS NULL
    OR m.air_quality IS NULL;

