import os
import psycopg2

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_URL")       # lo llamaste DB_URL en Secrets
DB_NAME = "postgres"                # cámbialo si usas otra base

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME,
        port=5432,
        sslmode="require"
    )

    print("✅ Conexión exitosa a Azure PostgreSQL (DEV)")

    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    print("Hora en la BD:", cur.fetchone())

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Error conectando a PostgreSQL (DEV):", e)
