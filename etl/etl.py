import csv
import psycopg2
from dateutil import parser
import logging
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONN_STRING = os.getenv("DATABASE_URL")


# =========================
# Configuration
# =========================
CSV_FILE = "senseYourCity_day.csv"
LOG_FILE = "etl/logs/etl_errors.log"

BATCH_SIZE = 200  # commit every 200 rows

# =========================
# Logging Setup
# =========================
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.ERROR,
    format="%(asctime)s - %(message)s"
)

# =========================
# Database Connection
# =========================
def get_connection():
    conn = psycopg2.connect(DB_CONN_STRING)
    conn.autocommit = False  # manual transaction control
    return conn

# =========================
# Transform Helpers
# =========================
def normalize_city(city):
    if not city or city.strip() == "":
        return None
    return city.strip().title()

def parse_timestamp(value):
    try:
        return parser.parse(value)
    except Exception:
        return None

def parse_float(value):
    try:
        return float(value)
    except Exception:
        return None

# =========================
# Load Helpers
# =========================
def get_or_create_city(cursor, city_name):
    cursor.execute(
        "SELECT city_id FROM city WHERE name = %s",
        (city_name,)
    )
    result = cursor.fetchone()
    if result:
        return result[0]

    cursor.execute(
        "INSERT INTO city (name) VALUES (%s) RETURNING city_id",
        (city_name,)
    )
    return cursor.fetchone()[0]

def insert_sensor_reading(cursor, city_id, timestamp):
    cursor.execute("""
        INSERT INTO sensor_reading (city_id, timestamp)
        VALUES (%s, %s)
        ON CONFLICT (city_id, timestamp) DO NOTHING
        RETURNING reading_id
    """, (city_id, timestamp))

    result = cursor.fetchone()
    if result:
        return result[0]

    cursor.execute("""
        SELECT reading_id
        FROM sensor_reading
        WHERE city_id = %s AND timestamp = %s
    """, (city_id, timestamp))
    return cursor.fetchone()[0]

def insert_measurement(cursor, reading_id, row):
    cursor.execute("""
        INSERT INTO measurement (
            reading_id,
            temperature,
            humidity,
            light,
            air_quality,
            sound,
            dust
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        reading_id,
        parse_float(row.get("temperature")),
        parse_float(row.get("humidity")),
        parse_float(row.get("light")),
        parse_float(row.get("airquality_raw")),
        parse_float(row.get("sound")),
        parse_float(row.get("dust")),
    ))

# =========================
# Main ETL Pipeline
# =========================
def run_etl():
    conn = get_connection()
    cursor = conn.cursor()

    success_count = 0
    error_count = 0
    batch_counter = 0

    with open(CSV_FILE, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row_num, row in enumerate(reader, start=1):
            try:
                city = normalize_city(row.get("city"))
                timestamp = parse_timestamp(row.get("timestamp"))

                if not city or not timestamp:
                    raise ValueError("Invalid city or timestamp")

                city_id = get_or_create_city(cursor, city)
                reading_id = insert_sensor_reading(cursor, city_id, timestamp)
                insert_measurement(cursor, reading_id, row)

                success_count += 1
                batch_counter += 1
                if success_count % 100 == 0:
                    print(f"Processed {success_count} rows...")

                # Commit in batches
                if batch_counter >= BATCH_SIZE:
                    conn.commit()
                    batch_counter = 0

            except Exception as e:
                error_count += 1
                logging.error(
                    f"Row {row_num} failed | Error: {e} | Data: {row}"
                )
                conn.rollback()  # rollback only the failed row transaction

    # Final commit
    conn.commit()

    cursor.close()
    conn.close()

    print("ETL completed successfully")
    print(f"Successful rows: {success_count}")
    print(f"Failed rows: {error_count}")

# =========================
# Entry Point
# =========================
if __name__ == "__main__":
    run_etl()
