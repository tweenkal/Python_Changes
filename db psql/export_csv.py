# export_all_queries_to_csv.py
from connection_DB import conn, cur  # apna connection import karo

# -----------------------------
# 1️⃣ LEFT JOIN → customer_orders.csv
# -----------------------------
copy_query1 = """
COPY (
    SELECT 
        c.id AS customer_id,
        c.name AS customer_name,
        COALESCE(SUM(p.price * o.quantity), 0) AS total_order_value
    FROM customers c
    LEFT JOIN orders o ON c.id = o.customer_id
    LEFT JOIN products p ON o.product_id = p.id
    GROUP BY c.id, c.name
    ORDER BY c.id
) TO STDOUT WITH CSV HEADER
"""

with open("customer_orders.csv", "w") as f1:
    cur.copy_expert(copy_query1, f1)
print("CSV file 'customer_orders.csv' created successfully!")

# -----------------------------
# 2️⃣ RIGHT JOIN → products_never_ordered.csv
# -----------------------------
copy_query2 = """
COPY (
    SELECT 
        p.id AS product_id,
        p.name AS product_name
    FROM products p
    RIGHT JOIN orders o ON p.id = o.product_id
    WHERE o.id IS NULL
    ORDER BY p.id
) TO STDOUT WITH CSV HEADER
"""

with open("products_never_ordered.csv", "w") as f2:
    cur.copy_expert(copy_query2, f2)
print("CSV file 'products_never_ordered.csv' created successfully!")

# -----------------------------
# 3️⃣ INNER JOIN → high_value_orders.csv
# -----------------------------
copy_query3 = """
COPY (
    SELECT 
        o.id AS order_id,
        c.name AS customer_name,
        p.name AS product_name,
        p.price,
        o.quantity,
        (p.price * o.quantity) AS total_value,
        o.order_date
    FROM orders o
    INNER JOIN customers c ON o.customer_id = c.id
    INNER JOIN products p ON o.product_id = p.id
    WHERE p.price > 50
    ORDER BY total_value DESC
) TO STDOUT WITH CSV HEADER
"""

with open("high_value_orders.csv", "w") as f3:
    cur.copy_expert(copy_query3, f3)
print("CSV file 'high_value_orders.csv' created successfully!")

# -----------------------------
# Close connection
# -----------------------------
cur.close()
conn.close()
print("All CSV files exported successfully!")
