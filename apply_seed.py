import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONN_STRING = os.getenv("DATABASE_URL")
conn = psycopg2.connect(
    DB_CONN_STRING
)

cursor = conn.cursor()

with open("sql/seed.sql", "r") as f:
    seed_sql = f.read()

cursor.execute(seed_sql)
conn.commit()

print("Seed data inserted successfully")

cursor.close()
conn.close()
