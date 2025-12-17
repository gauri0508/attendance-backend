import csv
import os
import psycopg2
from datetime import datetime
from dotenv import load_dotenv
from dateutil import parser


load_dotenv()

DB_URL = os.getenv("DATABASE_URL")
CSV_PATH = "task7/datasets/holiday_songs.csv"

def parse_date(date_str):
    if not date_str:
        return None
    return datetime.strptime(date_str, "%m/%d/%Y").date()

def parse_quake_date(date_str):
    try:
        return parser.parse(date_str).date()
    except Exception:
        return None


def run_etl():
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()

    inserted = 0
    skipped = 0

    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            try:
                cursor.execute(
                    """
                    INSERT INTO holiday_songs
                    (song_title, artist, year, chart_position, chart_date)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (
                        row["Song"],
                        row["Artist"],
                        int(row["Year"]),
                        int(row["Position"]) if row["Position"] else None,
                        parse_date(row["Chart Date"])
                    )
                )
                inserted += 1
            except Exception as e:
                skipped += 1
                conn.rollback()
                continue

    conn.commit()
    cursor.close()
    conn.close()

    print("ETL completed")
    print(f"Inserted rows: {inserted}")
    print(f"Skipped rows: {skipped}")








def run_earthquake_etl():
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()

    CSV_PATH_EQ = "task7/datasets/earthquakes_7_plus.csv"

    inserted = 0
    skipped = 0

    with open(CSV_PATH_EQ, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            quake_date = parse_quake_date(row["date"])

            # Skip rows where date is completely invalid
            if quake_date is None:
                skipped += 1
                continue

            try:
                cursor.execute(
                    """
                    INSERT INTO earthquakes
                    (quake_date, latitude, longitude, depth_km, magnitude)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (
                        quake_date,
                        float(row["latitude"]) if row["latitude"] else None,
                        float(row["longitude"]) if row["longitude"] else None,
                        float(row["depth"]) if row["depth"] else None,
                        float(row["magnitude"]) if row["magnitude"] else None,
                    )
                )
                inserted += 1
            except Exception:
                skipped += 1
                conn.rollback()
                continue

    conn.commit()
    cursor.close()
    conn.close()

    print("Earthquake ETL completed")
    print(f"Inserted rows: {inserted}")
    print(f"Skipped rows: {skipped}")



if __name__ == "__main__":
    run_etl()
    run_earthquake_etl()