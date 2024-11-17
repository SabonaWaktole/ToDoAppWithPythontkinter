from models.todo_model import TodoModel
from utils.file_handler import FileHandler

class TodoController:
    def __init__(self):
        self.model = TodoModel()
        self.file_handler = FileHandler()
        self.load_tasks()

    def add_task(self, task: str):
        self.model.add_task(task)
        self.save_tasks()

    def delete_task(self, task: str):
        self.model.delete_task(task)
        self.save_tasks()

    def get_tasks(self):
        return self.model.get_tasks()

    def save_tasks(self):
        self.file_handler.save_tasks(self.model.get_tasks())

    def load_tasks(self):
        tasks = self.file_handler.load_tasks()
        for task in tasks:
            self.model.add_task(task)
