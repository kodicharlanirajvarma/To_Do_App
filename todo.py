from tasks import Task
from datetime import datetime
from datetime import date

class ToDoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority, due_date):
        task = Task(title, priority, due_date)
        self.tasks.append(task)
        print("Task added successfully")

    def remove_task(self, index):
        try:
            if 0 <= index < len(self.tasks):
                removed = self.tasks.pop(index)
                print(f"'{removed.title}' is now removed")
            else:
                print("Invalid task number")
        except ValueError:
                print("Invalid input. Please enter a number.")
                return

    def complete_tasks(self, index):
        try:
            if 0 <= index < len(self.tasks):
                self.tasks[index].complete()
                print(f"'{self.tasks[index].title}' is completed")
            else:
                print("Invalid task number")
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

    def get_pending_task(self):
        pending = [task for task in self.tasks if task.status == "Pending"]
        return pending

    def get_completed_task(self):
        complete = [task for task in self.tasks if task.status == "Completed"]
        return complete

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found")
            return
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task.title} - {task.status}")
            print(f"Priority: {task.priority}")
            print(f"Due-date: {task.due_date}")
            print()

    def view_completed(self):
        found = False
        if not self.tasks:
            print("No tasks found")
            return
        display_index =1
        for index, task in enumerate(self.tasks, start=1):
            if task.status == "Completed":
                print(f"{display_index}. {task.title}")
                print(f"Priority: {task.priority}")
                print(f"Due-date: {task.due_date}")
                print()
                display_index +=1 
                found = True
        if not found:
            print("No tasks found")

    def edit_task(self, index, new_title):
        try:
            if 0 <= index < len(self.tasks):
                self.tasks[index].edit(new_title)
                print("task edited successfully")
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

    def reopen_task(self, index):
        try:
            self.tasks[index].reopen()
        except ValueError:
            print("Enter a valid number")
            return


    def delete_all_completed_tasks(self):
        completed_tasks = self.get_completed_task()
        if completed_tasks:
            for index in (len(self.tasks)-1, -1, -1):
                if self.tasks[index].status == "Completed":
                    removed = self.tasks.pop(index)
                    print(f"{removed.title} is now removed")
        else:
            print("No completed tasks to delete.")

    def delete_all_tasks(self):
        confirm = input("Are you sure you want to delete all tasks? (yes/no): ")
        confirm = confirm.strip().lower()  # Remove leading/trailing whitespace and convert to lowercase
        if confirm == "yes":
            self.tasks.clear()
            print("All tasks have been deleted.")
            # Save the updated tasks list after clearing
        else:
                print("Operation cancelled.")

    def task_statistics(self):
        completed_tasks = self.get_completed_task()
        pending_tasks = self.get_pending_task()
        if self.tasks:
            completion_rate = (len(completed_tasks) / len(self.tasks)) * 100
        else:
            completion_rate = 0.0
        print("Task Statistics:")
        print(f"Total tasks: {len(self.tasks)}")
        print(f"Pending tasks: {len(pending_tasks)}")
        print(f"Completed tasks: {len(completed_tasks)}")
        print(f"Completion rate: {completion_rate:.2f}%")

    def search_task(self, title):
        found = False
        for task in self.tasks:
            if title.lower() in task.title.lower():
                print(f"Task found")
                print(f"{task.title} - {task.status}")
                found = True
        if not found:
            print("No such task has been found")

    def sort_by_priority(self):
        priority_order = {
            "High": 1,
            "Medium" : 2,
            "Low" : 3
            }
        sorted_tasks = sorted(self.tasks, key=lambda task: priority_order.get(task.priority, 4)) 

        for index, task in enumerate(sorted_tasks, start=1):
            print(f"{index}. {task.title} - {task.priority}")

    def sort_by_due_date(self):
        sorted_tasks = sorted(self.tasks, key=lambda task: datetime.strptime(task.due_date, "%d-%m-%Y"))
        for index, task in enumerate(sorted_tasks, start=1):
            print(f"{index}. {task.title} - {task.due_date}")

    def overdue_tasks(self):
        found = False
        today = date.today()
        for index, task in enumerate(self.tasks, start=1):
            due_date = datetime.strptime(task.due_date, "%d-%m-%Y").date()
            if due_date < today:
                print(f"{index}. {task.title} - {task.status}")
                found = True
        if not found:
            print("No tasks are Overdue")














