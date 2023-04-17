# main.py

from tkinter import *
from gui.main_window import MainWindow

# Create an instance of Tk class
root = Tk()

# Set the window title
root.title("Inventory Management System")

# Create an instance of MainWindow class
main_window = MainWindow(root)

# Start the main event loop
root.mainloop()
