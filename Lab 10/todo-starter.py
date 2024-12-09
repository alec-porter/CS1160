import tkinter as tk
from tkinter import messagebox

# Create your classes here to implement the to-do list

class ToDoApp:

    # Some widgets are below to get you started
    # Add to following items:
    # - description label/entry
    # - date label/entry
    # - add task button
    # - complete task button
    # - display all tasks button
    def __init__(self, root):
        # Setting up the root
        self.root = root
        self.root.title("To-Do List")

        # Name label/entry
        self.label_name = tk.Label(root, text="Task Name:")
        self.label_name.pack()
        
        self.entry_name = tk.Entry(root)
        self.entry_name.pack()

        # Description label/entry

        # Time labels/entries
        self.label_due = tk.Label(root, text="Time:")
        self.label_due.pack()

        # Using a canvas is necessary to put grid widgets in between packed widgets
        self.time_canvas = tk.Canvas(root)
        
        self.entry_hour = tk.Entry(self.time_canvas)
        self.entry_hour.grid(row=0, column=0)
        
        self.label_colon = tk.Label(self.time_canvas, text=":")
        self.label_colon.grid(row=0, column=1)
        
        self.entry_minute = tk.Entry(self.time_canvas)
        self.entry_minute.grid(row=0, column=2)
        
        self.time_canvas.pack()

        # Dropdown menu for task class types

        self.var_type = tk.StringVar()
        self.var_type.set("Generic")

        self.dropdown_type = tk.OptionMenu(root, self.var_type, "Generic", "Personal", "School", "Work")
        self.dropdown_type.pack()

        # Buttons setup
        
        self.button_quit = tk.Button(root, text="Save and Quit", command=onQuit)
        self.button_quit.pack()

    # Methods for what the buttons should do
    def addTask(self):
        # Write this method to add a task to your todo list
        # You should not be able to add a task with a duplicate name or duplicate date + time
        pass

    def completeTask(self):
        # Write this method to remove a task from your todo list
        # Removing a todo that does not exist should not cause errors
        pass

    def displayTasks(self):
        # Rewrite this method to display the list of tasks to the 
        name = self.entry_name.get()
        messagebox.showinfo("Tasks", "You can replace this string to display your tasks. Also, here's what you typed inside of the task name:\n\n" + name)

def onQuit():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        # Put code here to save the todo list (use "todo.pickle")
        # Hint: Use pickle to make it easier
        root.destroy()

if __name__ == "__main__":
    # Load your To-do list from a file (do not prompt the user to enter in a file name, use "todo.pickle")
    # If the file does not exist do not show an error
    root = tk.Tk()
    app = ToDoApp(root)
    root.protocol("WM_DELETE_WINDOW", onQuit)
    root.mainloop()
