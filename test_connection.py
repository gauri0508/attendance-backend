import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONN_STRING = os.getenv("DATABASE_URL")
try:
    conn = psycopg2.connect(
        DB_CONN_STRING
    )
    print("Connected to PostgreSQL/NeonDB")
    conn.close()
except Exception as e:
    print("Connection failed:", e)
