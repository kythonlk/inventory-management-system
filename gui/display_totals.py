# display_totals.py

from data.inventory import Inventory

def display_totals(inventory):
    """
    Function to display the total prices and counts for each product category in the inventory.

    Args:
    - inventory (Inventory): The inventory object to calculate and display the totals.

    Returns:
    - None
    """
    # Get the total prices and counts for each product category from the inventory
    category_totals = inventory.calculate_category_totals()

    if category_totals:
        print("Total prices and counts by category:")
        for category, total in category_totals.items():
            print(f"Category: {category}, Total Price: {total['total_price']}, Total Count: {total['total_count']}")
    else:
        print("No products found in the inventory.")
