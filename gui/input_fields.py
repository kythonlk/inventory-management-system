# input_fields.py

import tkinter as tk

class InputFields(tk.Frame):
    """
    Class representing a custom input field with a label in the GUI.
    """
    def __init__(self, master, label_text, width=30):
        """
        Constructor for the InputField class.

        Args:
        - master (tk.Widget): The parent widget for the input field.
        - label_text (str): The text to be displayed as the label for the input field.
        - width (int): The width of the input field.
        """
        tk.Frame.__init__(self, master)
        self.label = tk.Label(self, text=label_text)
        self.label.pack(side=tk.LEFT, padx=(5, 10))
        self.entry = tk.Entry(self, width=width)
        self.entry.pack(side=tk.LEFT)

    def get_input(self):
        """
        Method to get the input value from the input field.

        Returns:
        - str: The input value from the input field.
        """
        return self.entry.get()

    def set_input(self, value):
        """
        Method to set the input value in the input field.

        Args:
        - value (str): The value to be set in the input field.
        """
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, value)
