import os
import psycopg2

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_URL = os.getenv("DB_URL")  # Example: "host=yourhost port=5432 dbname=yourdb"

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname='postgres',
        port=5432,
        sslmode="require"
    )
    print("✅ Conectado correctamente a PostgreSQL")

    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    result = cur.fetchone()
    print("Hora en la base de datos:", result)

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Error de conexión:", str(e))
