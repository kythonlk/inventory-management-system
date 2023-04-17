# buttons.py

import tkinter as tk

class Buttons(tk.Button):
    """
    Class representing a custom button in the GUI.
    """
    def __init__(self, master, text, command=None):
        """
        Constructor for the Button class.

        Args:
        - master (tk.Widget): The parent widget for the button.
        - text (str): The text to be displayed on the button.
        - command (function): The function to be executed when the button is clicked.
        """
        tk.Button.__init__(self, master, text=text, command=command, padx=10, pady=5)

    def set_text(self, text):
        """
        Sets the text of the button.

        Args:
        - text (str): The text to be displayed on the button.
        """
        self.configure(text=text)
        
    def set_command(self, command):
        """
        Sets the command of the button.

        Args:
        - command (function): The function to be executed when the button is clicked.
        """
        self.configure(command=command)

    def set_state(self, state):
        """
        Sets the state of the button.

        Args:
        - state (str): The state of the button.
        """
        self.configure(state=state)

    def set_background_color(self, color):
        """
        Sets the background color of the button.

        Args:
        - color (str): The color of the button.
        """
        self.configure(bg=color)
