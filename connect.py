import os
import psycopg2

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_URL")
DB_NAME = "postgres"  # cámbialo si usas otra BD

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME,
        port=5432,
        sslmode="require"
    )

    print(f"🔌 Conectado correctamente al servidor: {DB_HOST}")
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    print("⏱ Hora actual en BD:", cur.fetchone())

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Error conectando:", e)
    raise e
