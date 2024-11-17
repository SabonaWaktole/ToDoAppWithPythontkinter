import os
import json

class FileHandler:
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def save_tasks(self, tasks):
        with open(self.filename, "w") as file:
            json.dump(tasks, file)

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as file:
            return json.load(file)
