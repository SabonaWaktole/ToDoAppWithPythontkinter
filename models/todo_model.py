class TodoModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str):
        self.tasks.append(task)

    def delete_task(self, task: str):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks
