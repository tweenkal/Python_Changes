import psycopg2
from psycopg2 import sql  # safe dynamic SQL ke liye

# PostgreSQL connection details
host = "localhost"
user = "postgres"       # apna username
password = "admin123"   # apna password
port = "5432"
new_db_name = "shopdb"  # jo database create karna hai

# Connect to default 'postgres' database
conn = psycopg2.connect(
    host=host,
    database="postgres",  # default DB for creating new DB
    user=user,
    password=password,
    port=port
)

conn.autocommit = True  # Required for CREATE DATABASE
cur = conn.cursor()

# Safe query to create database
cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_db_name)))
print(f"Database '{new_db_name}' created successfully!")

# Close connection
cur.close()
conn.close()
