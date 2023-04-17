# remove_product.py

from data.inventory import Inventory

def remove_product(inventory, product_id):
    """
    Function to remove a product from the inventory based on its ID.

    Args:
    - inventory (Inventory): The inventory object to remove the product from.
    - product_id (str): The ID of the product to be removed.

    Returns:
    - None
    """
    # Check if the product ID exists in the inventory
    if inventory.has_product(product_id):
        # Remove the product from the inventory
        inventory.remove_product(product_id)
        print(f"Product with ID '{product_id}' has been removed from the inventory.")
    else:
        print(f"No product found with ID '{product_id}'.")
