def sales_analysis(sales_data):
    """
       Calculate total sales, average sales, and highest-selling product.
    """
    total_sales = 0
    product_total = {}

    # Step 1: Total sales aur product-wise sales
    for sale in sales_data:
        total_sales += sale["sale_amount"]

        pid = sale["product_id"]
        pname = sale["product_name"]

        if pid not in product_total:
            product_total[pid] = {"name": pname, "amount": 0}

        product_total[pid]["amount"] += sale["sale_amount"]

    # Step 2: Average sales
    average_sales = total_sales // len(sales_data)

    # Step 3: Highest-selling product
    highest_pid = None
    highest_amount = 0

    for pid in product_total:
        if product_total[pid]["amount"] > highest_amount:
            highest_amount = product_total[pid]["amount"]
            highest_pid = pid

    return {
        "Total Sales": total_sales,
        "Average Sales": average_sales,
        "Highest-Selling Product": {
            "product_id": highest_pid,
            "product_name": product_total[highest_pid]["name"]
        }
    }


sales_data = [
    {"product_id": 101, "product_name": "Smartphone", "sale_amount": 500,
     "sale_date": "2025-01-01"},
    {"product_id": 102, "product_name": "Laptop", "sale_amount": 300,
     "sale_date": "2025-01-02"},
    {"product_id": 101, "product_name": "Smartphone", "sale_amount": 400,
     "sale_date": "2025-01-03"},
    {"product_id": 103, "product_name": "Smartwatch", "sale_amount": 700,
     "sale_date": "2025-01-04"}
]

print(sales_analysis(sales_data))
