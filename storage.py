import json 
import os
from tasks import Task

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "tasks.json")

class Storage:
    def save(self, tasks):
        data = []
        for task in tasks:
            data.append(task.to_dict())
        with open(FILE_PATH, "w") as file:
            json.dump(data, file, indent = 4)

    def load_tasks(self):
        try:
            with open(FILE_PATH,"r") as file:
                data = json.load(file)
                tasks=[]
                for item in data:
                    task = Task(
                        item["title"],
                        item["priority"],
                        item["due_date"]
                        )
                    task.status = item["status"]
                    tasks.append(task)
                return tasks
        except FileNotFoundError:
            return []