# display_totals_window.py

from tkinter import *
from tkinter.scrolledtext import ScrolledText

class DisplayTotalsWindow(Toplevel):
    def __init__(self, category_totals):
        super().__init__()
        self.title("Display Totals")
        
        # Create scrolled text widget to display totals
        self.scrolled_text = ScrolledText(self, width=50, height=20)
        self.scrolled_text.pack(padx=10, pady=10, fill=BOTH, expand=True)

        # Populate the scrolled text widget with category totals
        self._populate_category_totals(category_totals)

    def _populate_category_totals(self, category_totals):
        for category, total in category_totals.items():
            self.scrolled_text.insert(END, f"Category: {category}\n")
            self.scrolled_text.insert(END, f"Total Count: {total['count']}\n")
            self.scrolled_text.insert(END, f"Total Price: {total['price']}\n")
            self.scrolled_text.insert(END, "\n")
        self.scrolled_text.config(state=DISABLED)
