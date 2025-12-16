import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONN_STRING = os.getenv("DATABASE_URL")
conn = psycopg2.connect(
    DB_CONN_STRING
)

cursor = conn.cursor()

cursor.execute("""
SELECT c.name, sr.timestamp, m.temperature, m.humidity
FROM city c
JOIN sensor_reading sr ON c.city_id = sr.city_id
JOIN measurement m ON sr.reading_id = m.reading_id;
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()
