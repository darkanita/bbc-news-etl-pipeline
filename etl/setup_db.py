import psycopg2
import os

def load_sql(path, schema_name):
    with open(path, "r") as f:
        sql = f.read()
    return sql.replace("{{SCHEMA_NAME}}", schema_name)

def run():
    schema = os.getenv("SCHEMA_NAME")
    if not schema:
        raise Exception("SCHEMA_NAME environment variable not set")

    conn = psycopg2.connect(
        host=os.getenv("AZURE_PG_HOST"),
        user=os.getenv("AZURE_PG_USER"),
        password=os.getenv("AZURE_PG_PASSWORD"),
        dbname=os.getenv("AZURE_PG_DB"),
        port=os.getenv("AZURE_PG_PORT", "5432")
    )
    conn.autocommit = True
    cur = conn.cursor()

    # Run schema creation
    schema_sql = load_sql("sql/create_schemas.sql", schema)
    cur.execute(schema_sql)

    # Run table creation
    tables_sql = load_sql("sql/create_tables.sql", schema)
    cur.execute(tables_sql)

    print(f"Schema and tables successfully created under schema: {schema}")

    cur.close()
    conn.close()

if __name__ == "__main__":
    run()
