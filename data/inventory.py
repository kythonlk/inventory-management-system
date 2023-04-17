# inventory.py

class Product:
    """
    Class representing a product in the inventory.
    """
    def __init__(self, name, id, price, category, brand):
        """
        Constructor for the Product class.

        Args:
        - name (str): The name of the product.
        - id (str): The ID of the product.
        - price (float): The price of the product.
        - category (str): The category of the product.
        - brand (str): The brand of the product.
        """
        self.name = name
        self.id = id
        self.price = price
        self.category = category
        self.brand = brand

class Inventory:
    """
    Class representing the inventory for managing products.
    """
    def __init__(self):
        """
        Constructor for the Inventory class.
        """
        self.products = []

    def add_product(self, product):
        """
        Method to add a product to the inventory.

        Args:
        - product (Product): The product object to be added.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Method to remove a product from the inventory.

        Args:
        - product (Product): The product object to be removed.
        """
        self.products.remove(product)

    def search_product(self, product_id):
        """
        Method to search for a product in the inventory by ID.

        Args:
        - product_id (str): The ID of the product to be searched.

        Returns:
        - Product: The product object if found, None otherwise.
        """
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def get_total_price_by_category(self, category):
        """
        Method to calculate the total price of products in a given category.

        Args:
        - category (str): The category of the products to be calculated.

        Returns:
        - float: The total price of products in the given category.
        """
        total_price = 0.0
        for product in self.products:
            if product.category == category:
                total_price += product.price
        return total_price

    def get_total_price(self):
        """
        Method to calculate the total price of all products in the inventory.

        Returns:
        - float: The total price of all products in the inventory.
        """
        total_price = 0.0
        for product in self.products:
            total_price += product.price
        return total_price

    def get_product_count(self):
        """
        Method to get the total count of products in the inventory.

        Returns:
        - int: The total count of products in the inventory.
        """
        return len(self.products)

