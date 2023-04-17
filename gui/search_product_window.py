# search_product_window.py

from tkinter import *
from gui.input_fields import InputFields
from gui.buttons import Buttons

class SearchProductWindow(Toplevel):
    def __init__(self, callback):
        super().__init__()
        self.title("Search Product")
        self.callback = callback

        # Create input fields
        self.input_fields = InputFields(self, show_id=True)

        # Create buttons
        self.buttons = Buttons(self, "Search", self._on_search_button_click)

    def _on_search_button_click(self):
        # Get input value from input field
        product_id = self.input_fields.get_product_id()

        # Call the callback function to handle product search
        self.callback(product_id)

        # Close the window after searching for the product
        self.destroy()
