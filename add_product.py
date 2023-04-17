# add_product.py

from data.inventory import Inventory

def add_product(inventory, product):
    """
    Function to add a product to the inventory.

    Args:
    - inventory (Inventory): The inventory object to add the product to.
    - product (dict): A dictionary containing the product details, such as name, ID, price, category, and brand.

    Returns:
    - None
    """
    # Extract the product details from the dictionary
    product_name = product['name']
    product_id = product['id']
    product_price = product['price']
    product_category = product['category']
    product_brand = product['brand']

    # Create a new Product object with the extracted details
    new_product = Product(product_name, product_id, product_price, product_category, product_brand)

    # Add the new product to the inventory
    inventory.add_product(new_product)

    print(f"Product '{product_name}' with ID '{product_id}' has been added to the inventory.")
