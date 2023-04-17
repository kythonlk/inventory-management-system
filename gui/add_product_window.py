# add_product_window.py

from tkinter import *
from gui.input_fields import InputFields
from gui.buttons import Buttons

class AddProductWindow(Toplevel):
    def __init__(self, callback):
        super().__init__()
        self.title("Add Product")
        self.callback = callback

        # Create input fields
        self.input_fields = InputFields(self)

        # Create buttons
        self.buttons = Buttons(self, "Add", self._on_add_button_click)

    def _on_add_button_click(self):
        # Get input values from input fields
        product_name = self.input_fields.get_product_name()
        product_id = self.input_fields.get_product_id()
        product_price = self.input_fields.get_product_price()
        product_category = self.input_fields.get_product_category()
        product_brand = self.input_fields.get_product_brand()

        # Add product to inventory (data layer)
        # Call the callback function to handle the data
        self.callback(product_name, product_id, product_price, product_category, product_brand)

        # Close the window after adding the product
        self.destroy()
