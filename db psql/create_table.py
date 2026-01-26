from DB_Connection import conn, cur

# PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    database="shopdb",
    user="postgres",
    password="admin123",
    port="5432"
)

cur = conn.cursor()

# -----------------------------
# Create tables
# -----------------------------

# Customers table
cur.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
""")

# Products table
cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price NUMERIC(10,2)
);
""")

# Orders table with order_date
cur.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    product_id INT REFERENCES products(id),
    quantity INT NOT NULL,
    order_date DATE DEFAULT CURRENT_DATE  -- new column added
);
""")

conn.commit()
print("Tables created successfully with order_date in orders!")

cur.close()
conn.close()
