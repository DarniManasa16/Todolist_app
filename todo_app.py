import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkfont
import sys

print(f"Python version: {sys.version}")
print("Starting application...")

class TodoApp:
    def __init__(self, root):
        print("Initializing TodoApp...")
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x500")
        self.root.resizable(True, True)
        
        # Configure style
        style = ttk.Style()
        style.configure("Custom.TButton", padding=5, font=('Helvetica', 10))
        
        # Create main frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create and configure the listbox
        self.task_listbox = tk.Listbox(self.main_frame, font=('Helvetica', 11))
        self.task_listbox.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Create input frame
        input_frame = ttk.Frame(self.main_frame)
        input_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Create entry widget
        self.task_entry = ttk.Entry(input_frame, font=('Helvetica', 11))
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        # Create buttons frame
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(fill=tk.X)
        
        # Create buttons
        ttk.Button(button_frame, text="Add Task", command=self.add_task, style="Custom.TButton").pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="Mark Completed", command=self.mark_completed, style="Custom.TButton").pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="Remove Task", command=self.remove_task, style="Custom.TButton").pack(side=tk.LEFT, padx=2)
        
        # Bind Enter key to add_task
        self.task_entry.bind('<Return>', lambda e: self.add_task())
        
        # Initialize tasks list
        self.tasks = []
        print("TodoApp initialized successfully")
        
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_listbox.insert(tk.END, f"☐ {task}")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
            
    def mark_completed(self):
        try:
            selection = self.task_listbox.curselection()
            if not selection:
                messagebox.showwarning("Warning", "Please select a task!")
                return
                
            index = selection[0]
            if not self.tasks[index]["completed"]:
                self.tasks[index]["completed"] = True
                task_text = self.task_listbox.get(index)
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, f"✓ {task_text[2:]}")
                self.task_listbox.selection_clear(0, tk.END)
        except IndexError:
            messagebox.showerror("Error", "Invalid selection!")
            
    def remove_task(self):
        try:
            selection = self.task_listbox.curselection()
            if not selection:
                messagebox.showwarning("Warning", "Please select a task!")
                return
                
            index = selection[0]
            self.task_listbox.delete(index)
            self.tasks.pop(index)
        except IndexError:
            messagebox.showerror("Error", "Invalid selection!")

def main():
    print("Creating main window...")
    try:
        root = tk.Tk()
        app = TodoApp(root)
        print("Starting mainloop...")
        root.mainloop()
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main() 
    #cd "C:\Users\manas\To do List app"