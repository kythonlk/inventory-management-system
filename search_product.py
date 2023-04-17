# search_product.py

from data.inventory import Inventory

def search_product(inventory, product_name):
    """
    Function to search for a product in the inventory based on its name.

    Args:
    - inventory (Inventory): The inventory object to search for the product.
    - product_name (str): The name of the product to be searched.

    Returns:
    - None
    """
    # Search for the product by name in the inventory
    found_products = inventory.search_product_by_name(product_name)

    if found_products:
        print(f"Products with name '{product_name}' found in the inventory:")
        for product in found_products:
            print(f"ID: {product.product_id}, Name: {product.product_name}, Price: {product.product_price}, "
                f"Category: {product.product_category}, Brand: {product.product_brand}")
    else:
        print(f"No products found with name '{product_name}' in the inventory.")
