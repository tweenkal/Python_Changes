import psycopg
print(psycopg.__version__)
import csv

# ---------- STEP 1: Connect to PostgreSQL ----------
conn = psycopg.connect(
    dbname="office_db",
    user="postgres",
    password="mypassword123",
    host="localhost",
    port=5432
)

# verify
# psql -U postgres -d office_db

# ALTER USER postgres WITH PASSWORD 'mypassword123';
# pg_ctl status

# ---------- STEP 2: Use context manager for cursor ----------
with conn.cursor() as cur:

    # ---------- QUERY 1: LEFT JOIN ----------
    query_left_join = """
    SELECT 
        c.id AS customer_id,
        c.name AS customer_name,
        COALESCE(SUM(p.price * o.quantity), 0) AS total_order_value
    FROM customers c
    LEFT JOIN orders o ON c.id = o.customer_id
    LEFT JOIN products p ON o.product_id = p.id
    GROUP BY c.id, c.name
    ORDER BY total_order_value DESC;
    """
    cur.execute(query_left_join)
    result_left_join = cur.fetchall()
    print("LEFT JOIN Result:", result_left_join)

    # ---------- QUERY 2: RIGHT JOIN ----------
    query_right_join = """
    SELECT 
        p.id AS product_id,
        p.name AS product_name
    FROM products p
    RIGHT JOIN orders o ON p.id = o.product_id
    WHERE o.id IS NULL;
    """
    cur.execute(query_right_join)
    result_right_join = cur.fetchall()
    print("RIGHT JOIN Result:", result_right_join)

    # ---------- QUERY 3: INNER JOIN ----------
    query_inner_join = """
    SELECT 
        o.id AS order_id,
        c.name AS customer_name,
        p.name AS product_name,
        o.quantity,
        p.price,
        (p.price * o.quantity) AS total_value
    FROM orders o
    INNER JOIN customers c ON o.customer_id = c.id
    INNER JOIN products p ON o.product_id = p.id
    WHERE p.price > 50
    ORDER BY total_value DESC;
    """
    cur.execute(query_inner_join)
    result_inner_join = cur.fetchall()
    print("INNER JOIN Result:", result_inner_join)

    # ---------- STEP 3: Save results to CSV ----------
    def save_to_csv(filename, data, headers):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(data)

    save_to_csv('left_join.csv', result_left_join, ['customer_id', 'customer_name', 'total_order_value'])
    save_to_csv('right_join.csv', result_right_join, ['product_id', 'product_name'])
    save_to_csv('inner_join.csv', result_inner_join, ['order_id', 'customer_name', 'product_name', 'quantity', 'price', 'total_value'])

# ---------- STEP 4: Close the connection ----------
conn.close()
print("All queries executed and CSV files created successfully!")
