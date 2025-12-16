-- City summary report function

CREATE OR REPLACE FUNCTION get_city_summary(p_city TEXT)
RETURNS TABLE (
    city TEXT,
    total_readings BIGINT,
    avg_temperature NUMERIC
)
AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.name,
        COUNT(sr.reading_id),
        ROUND(AVG(m.temperature)::NUMERIC, 2)
    FROM city c
    JOIN sensor_reading sr ON c.city_id = sr.city_id
    JOIN measurement m ON sr.reading_id = m.reading_id
    WHERE c.name = p_city
    GROUP BY c.name;
END;
$$ LANGUAGE plpgsql;

