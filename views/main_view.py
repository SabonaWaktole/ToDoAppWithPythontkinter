import tkinter as tk
from tkinter import messagebox
from controllers.todo_controller import TodoController


class TodoApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("To-Do Application")
        self.controller = TodoController()

        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(self.root, width=50, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.load_tasks()

    def run(self):
        self.root.mainloop()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.controller.add_task(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")

    def delete_task(self):
        selected_task = self.task_listbox.get(tk.ACTIVE)
        if selected_task:
            self.controller.delete_task(selected_task)
            self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "No task selected!")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        tasks = self.controller.get_tasks()
        for task in tasks:
            self.task_listbox.insert(tk.END, task)

    def load_tasks(self):
        tasks = self.controller.get_tasks()
        for task in tasks:
            self.task_listbox.insert(tk.END, task)
