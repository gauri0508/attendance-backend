import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONN_STRING = os.getenv("DATABASE_URL")
conn = psycopg2.connect(
    DB_CONN_STRING
)

cursor = conn.cursor()

with open("sql/schema.sql", "r") as f:
    schema_sql = f.read()

cursor.execute(schema_sql)
conn.commit()

print("Schema applied successfully")

cursor.execute("""
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';
""")

print(cursor.fetchall())

cursor.close()
conn.close()



