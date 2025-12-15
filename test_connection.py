import psycopg2

try:
    conn = psycopg2.connect(
        "postgresql://neondb_owner:npg_ECOd1BrYaX2S@ep-winter-unit-a4fmzajh-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
    )
    print("Connected to PostgreSQL/NeonDB")
    conn.close()
except Exception as e:
    print("Connection failed:", e)
