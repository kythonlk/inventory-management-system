# main_window.py

import tkinter as tk
from gui.add_product_window import AddProductWindow
from gui.remove_product_window import RemoveProductWindow
from gui.search_product_window import SearchProductWindow
from gui.display_totals_window import DisplayTotalsWindow

class MainWindow(tk.Tk):
    """
    Class representing the main window of the inventory management system.
    """
    def __init__(self, inventory):
        """
        Constructor for the main window.

        Args:
        - inventory (Inventory): The inventory object to be used in the GUI.
        """
        tk.Tk.__init__(self)
        self.inventory = inventory
        self.title("Inventory Management System")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        """
        Method to create the widgets for the main window.
        """
        add_product_button = tk.Button(self, text="Add Product", command=self.open_add_product_window)
        add_product_button.pack(pady=10)

        remove_product_button = tk.Button(self, text="Remove Product", command=self.open_remove_product_window)
        remove_product_button.pack(pady=10)

        search_product_button = tk.Button(self, text="Search Product", command=self.open_search_product_window)
        search_product_button.pack(pady=10)

        display_totals_button = tk.Button(self, text="Display Totals", command=self.open_display_totals_window)
        display_totals_button.pack(pady=10)

    def open_add_product_window(self):
        """
        Method to open the add product window.
        """
        add_product_window = AddProductWindow(self.inventory)
        add_product_window.mainloop()

    def open_remove_product_window(self):
        """
        Method to open the remove product window.
        """
        remove_product_window = RemoveProductWindow(self.inventory)
        remove_product_window.mainloop()

    def open_search_product_window(self):
        """
        Method to open the search product window.
        """
        search_product_window = SearchProductWindow(self.inventory)
        search_product_window.mainloop()

    def open_display_totals_window(self):
        """
        Method to open the display totals window.
        """
        display_totals_window = DisplayTotalsWindow(self.inventory)
        display_totals_window.mainloop()
