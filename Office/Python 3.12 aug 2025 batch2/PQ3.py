"""
    Increase product prices by 10% and keep only products with updated price > 100.
"""
products = [
    {"name": "Laptop", "price": 950},
    {"name": "Mouse", "price": 40},
    {"name": "Keyboard", "price": 80},
    {"name": "Monitor", "price": 120}
]


def update_and_filter_products(product_list):
    """Increase prices by 10% and keep products with price > 100."""
    updated_products = list(
        map(lambda product: {"name": product["name"],
                             "price": product["price"] * 1.1}, product_list)
    )

    filtered_products = list(
        filter(lambda product: product["price"] > 100, updated_products)
    )
    return filtered_products


result = update_and_filter_products(products)
print(result)
