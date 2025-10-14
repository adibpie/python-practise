import tkinter as tk
from tkinter import messagebox

# --- Helper Functions ---

def add_task():
    """Gets a task from the entry box and adds it to the listbox."""
    task = task_entry.get()
    # Ensure the user has typed something
    if task:
        tasks_listbox.insert(tk.END, task)
        # Clear the entry box after adding the task
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    """Deletes the currently selected task from the listbox."""
    try:
        # Get the index of the selected task
        selected_task_index = tasks_listbox.curselection()[0]
        # Delete the task at that index
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        # This happens if the delete button is clicked with no task selected
        messagebox.showwarning("Warning", "You must select a task to delete.")

def mark_task_done():
    """Marks the selected task as done by adding a checkmark and changing its color."""
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        # Add a checkmark if it's not already there
        if not task.startswith("✓ "):
            marked_task = "✓ " + task
            # Delete the old task and insert the marked one
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, marked_task)
            # Change the item's color to green
            tasks_listbox.itemconfig(selected_task_index, {'fg': 'green'})
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as done.")

def save_tasks():
    """Saves all current tasks to a text file."""
    tasks = tasks_listbox.get(0, tk.END)
    # 'with' statement handles opening and closing the file automatically
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Info", "Tasks have been saved.")

def load_tasks():
    """Loads tasks from the text file when the app starts."""
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task = line.strip() # .strip() removes the newline character
                tasks_listbox.insert(tk.END, task)
                # If the task was saved as 'done', apply the green color
                if task.startswith("✓ "):
                    # Find the index of the newly inserted item to color it
                    last_item_index = tasks_listbox.size() - 1
                    tasks_listbox.itemconfig(last_item_index, {'fg': 'green'})
    except FileNotFoundError:
        # This is fine, it just means it's the first time running the app
        print("No tasks file found. Starting with an empty list.")

# --- Main GUI Setup ---

# 1. Create the main window
root = tk.Tk()
root.title("Simple To-Do List")
root.geometry("450x550") # Adjusted size for more buttons

# 2. Create a frame to hold all the widgets for better layout management
frame = tk.Frame(root)
frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# 3. Create the Listbox widget to display tasks
tasks_listbox = tk.Listbox(
    frame,
    font=("Helvetica", 12),
    height=15,
    selectbackground="#a6a6a6", # Color for the selected item
    selectforeground="white"
)
tasks_listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# 4. Create a scrollbar for the Listbox
scrollbar = tk.Scrollbar(tasks_listbox)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tasks_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks_listbox.yview)

# 5. Create the Entry widget for new tasks
task_entry = tk.Entry(
    frame,
    font=("Helvetica", 12)
)
task_entry.pack(fill=tk.X, pady=(10, 5))

# 6. Create a frame for the buttons to keep them organized
button_frame = tk.Frame(frame)
button_frame.pack(fill=tk.X)

# 7. Create the Button widgets
add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2)

mark_done_button = tk.Button(button_frame, text="Mark as Done", command=mark_task_done)
mark_done_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2)

save_button = tk.Button(frame, text="Save Tasks", command=save_tasks)
save_button.pack(fill=tk.X, pady=(5, 0))

# --- Program Start ---

# Load any saved tasks right when the program opens
load_tasks()

# Start the main event loop to run the application
root.mainloop()

