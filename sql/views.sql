-- City-wise daily average metrics (VIEW)
CREATE OR REPLACE VIEW city_daily_avg_metrics AS
SELECT
    c.name AS city,
    DATE(sr.timestamp) AS day,
    ROUND(AVG(m.temperature), 2) AS avg_temperature,
    ROUND(AVG(m.humidity), 2) AS avg_humidity,
    ROUND(AVG(m.air_quality), 2) AS avg_air_quality
FROM city c
JOIN sensor_reading sr ON c.city_id = sr.city_id
JOIN measurement m ON sr.reading_id = m.reading_id
GROUP BY c.name, DATE(sr.timestamp);
