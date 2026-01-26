sales_data = [
    {"product_id": 101, "product_name": "Smartphone", "sale_amount": 500,
     "sale_date": "2025-01-01"},
    {"product_id": 102, "product_name": "Laptop", "sale_amount": 300,
     "sale_date": "2025-01-01"},
    {"product_id": 101, "product_name": "Smartphone", "sale_amount": 400,
     "sale_date": "2025-01-02"},
    {"product_id": 103, "product_name": "Smartwatch", "sale_amount": 700,
     "sale_date": "2025-01-02"},
]


def sales_trend_analysis(sales_data):
    """Calculate total sales per day and identify the highest-selling day."""
    total_sales_per_day = {}

    for record in sales_data:
        date = record["sale_date"]
        amount = record["sale_amount"]
        total_sales_per_day[date] = total_sales_per_day.get(date, 0) + amount

    highest_selling_day = max(total_sales_per_day, key=total_sales_per_day.get)

    return {
        "Total Sales Per Day": total_sales_per_day,
        "Highest-Selling Day": highest_selling_day
    }


result = sales_trend_analysis(sales_data)
print(result)
