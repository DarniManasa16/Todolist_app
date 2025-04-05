import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # Hide the main window
messagebox.showinfo("Test", "Tkinter is working!")
root.destroy() 