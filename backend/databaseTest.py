import psycopg2

DB_PARAMS = {
    "database": "premierleague_data",
    "user": "postgres",
    "password": "password",
    "host": "localhost",
    "port": "5432"
}

try:
    connection = psycopg2.connect(
        database=DB_PARAMS["database"],
        user=DB_PARAMS["user"],
        password=DB_PARAMS["password"],
        host=DB_PARAMS["host"],
        port=DB_PARAMS["port"]
    )
    print("Database connection successful!")
    connection.close()

except Exception as e:
    print(f"Database connection failed: {e}")
