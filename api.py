from flask import Flask, request, jsonify
import psycopg2
from dateutil import parser
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONN_STRING = os.getenv("DATABASE_URL")

app = Flask(__name__)


def get_connection():
    conn = psycopg2.connect(DB_CONN_STRING)
    conn.autocommit = False
    return conn

def normalize_city(city):
    if not city or city.strip() == "":
        return None
    return city.strip().title()

def parse_float(value):
    try:
        return float(value)
    except Exception:
        return None

@app.route("/register-reading", methods=["POST"])
def register_reading():
    data = request.json

    try:
        city = normalize_city(data.get("city"))
        timestamp = parser.parse(data.get("timestamp"))

        if not city or not timestamp:
            return jsonify({"error": "Invalid city or timestamp"}), 400

        conn = get_connection()
        cursor = conn.cursor()

        # Insert or get city
        cursor.execute(
            "SELECT city_id FROM city WHERE name = %s", (city,)
        )
        row = cursor.fetchone()
        if row:
            city_id = row[0]
        else:
            cursor.execute(
                "INSERT INTO city (name) VALUES (%s) RETURNING city_id",
                (city,)
            )
            city_id = cursor.fetchone()[0]

        # Insert sensor reading
        cursor.execute("""
            INSERT INTO sensor_reading (city_id, timestamp)
            VALUES (%s, %s)
            ON CONFLICT (city_id, timestamp) DO NOTHING
            RETURNING reading_id
        """, (city_id, timestamp))

        row = cursor.fetchone()
        if row:
            reading_id = row[0]
        else:
            cursor.execute("""
                SELECT reading_id FROM sensor_reading
                WHERE city_id = %s AND timestamp = %s
            """, (city_id, timestamp))
            reading_id = cursor.fetchone()[0]

        # Insert measurement
        cursor.execute("""
            INSERT INTO measurement (
                reading_id, temperature, humidity, light,
                air_quality, sound, dust
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            reading_id,
            parse_float(data.get("temperature")),
            parse_float(data.get("humidity")),
            parse_float(data.get("light")),
            parse_float(data.get("airquality_raw")),
            parse_float(data.get("sound")),
            parse_float(data.get("dust")),
        ))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"status": "success"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=5000, debug=True)
