from connection_DB import conn, cur

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
# Insert sample data into customers
# -----------------------------
cur.execute("""
INSERT INTO customers (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Charlie', 'charlie@example.com');
""")

# -----------------------------
# Insert sample data into products
# -----------------------------
cur.execute("""
INSERT INTO products (name, price) VALUES
('Mobile', 30),
('Laptop', 70),
('TV', 90);
""")

# -----------------------------
# Insert sample data into orders
# -----------------------------
cur.execute("""
INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES
(1, 1, 1, '2025-01-01'),   
(2, 1, 3, '2026-01-02');
""")

# Commit changes
conn.commit()
print("Sample data inserted successfully!")

# Close connection
cur.close()
conn.close()
