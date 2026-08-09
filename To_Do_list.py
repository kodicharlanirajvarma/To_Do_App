import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "tasks.json")

def load_tasks():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        print("Error: tasks.json is not a valid JSON file. Starting with an empty task list.")
        return []

tasks = load_tasks()

def save_tasks():
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file)

def add_task(task):
    if  task.strip():
        t = {
            "task" : task,
            "status" : "Pending"
        }
    else:
        print("Task cannot be empty")
        return
    tasks.append(t)
    print(f"Task:{task} is successfully added")
    save_tasks()

def view_tasks():
    if tasks:
        found = False 
        display_index = 1  # Initialize display index for user-friendly numbering
        for index, task in enumerate(tasks):
            if task["status"] == "Pending":
                print(f"{display_index}. {task['task']} - {task['status']}")
                found = True
                display_index += 1
        if not found:
            print("No Pending Tasks were found")
    else:
        print("No Tasks were found")

def remove_task(index):
    pending_tasks = get_pending_tasks()  # Refresh the pending_tasks list
    if 0 <= index < len(pending_tasks):
        actual_task = pending_tasks[index]
        removed = tasks.pop(actual_task)
        print(f"{removed['task']} is now removed")
        save_tasks()  # Save the updated tasks list after removal
    else:
        print("Enter a valid index number")

def complete_task(index):
    pending_tasks = get_pending_tasks()  # Refresh the pending_tasks list
    if 0 <=  index < len(pending_tasks):
        actual_task = pending_tasks[index]
        tasks[actual_task]["status"] = "Completed"
        print(f"{tasks[actual_task]['task']} is completed")
        save_tasks()
    else:
        print("Invalid task number")

def get_pending_tasks():
    pending_tasks = []
    for index, task in enumerate(tasks):
        if task["status"] == "Pending":
            pending_tasks.append(index)
    return pending_tasks

def get_completed_tasks():
    completed_tasks = []
    for index, task in enumerate(tasks):
        if task["status"] == "Completed":
            completed_tasks.append(index)
    return completed_tasks

def view_completed():
    found = False
    display_index = 1  # Initialize display index for user-friendly numbering
    for task in tasks:
        if task["status"] == "Completed":
            print(f"{display_index}. {task['task']} - {task['status']}")
            found = True
            display_index += 1
    if not found:
        print("No Completed Tasks were found")

def edit_task(index, new_task):
    if not new_task.strip():
        print("Task cannot be empty")
        return
    if 0 <= index < len(tasks):
        actual_task = tasks[index]
        tasks[actual_task]["task"] = new_task
        print(f"Task at index {actual_task} has been updated to: {new_task}")
        save_tasks()  # Save the updated tasks list after editing
    else:
        print("Invalid task number")

def view_all_tasks():
    print("Your tasks are: ")
    if tasks:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['task']} - {task['status']}")
    else:
        print("No Tasks were found")

def reopen_task(index):
    completed_tasks = get_completed_tasks()  # Refresh the completed_tasks list
    if 0 <= index < len(completed_tasks):
        actual_task = completed_tasks[index]
        tasks[actual_task]["status"] = "Pending"
        print(f"{tasks[actual_task]['task']} is reopened")
        save_tasks()
    else:
        print("Invalid task number")

print("Welcome to my to-do list app")
while True:
    print("Choose your desired operation")
    print("1. Add tasks")
    print("2. View tasks")
    print("3. View completed tasks")
    print("4. View all tasks")
    print("5. Remove task")
    print("6. Complete task")
    print("7. Edit task")
    print("8. Reopen a completed task")
    print("9. Delete all completed tasks")
    print("10. Delete all tasks")
    print("11. Task statistics")
    print("12. Exit")
    try:
        choice = int(input("Enter your option number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    match choice:
        case 1:
            task = input("Enter your task to add: ")
            add_task(task)
        case 2:
            view_tasks()
        case 3:
            view_completed()
        case 4:
            view_all_tasks()
        case 5:
            try:
                index = int(input("Enter your task number you want to remove: "))
                remove_task(index-1)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        case 6:
            try:
                index = int(input("Enter the task number you want to complete: "))
                complete_task(index-1)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        case 7:
            try:
                view_all_tasks()
                index = int(input("Enter the task number you want to edit: "))
                new_task = input("Enter the new task: ")
                edit_task(index-1, new_task)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        case 8:
            try:
                index = int(input("Enter the task number you want to reopen: "))
                reopen_task(index-1)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        case 9:
            completed_tasks = get_completed_tasks()
            if completed_tasks:
                for index in sorted(completed_tasks, reverse=True):
                    removed = tasks.pop(index)
                    print(f"{removed['task']} is now removed")
                    save_tasks()  # Save the updated tasks list after removal
            else:
                print("No completed tasks to delete.")
        case 10:
            confirm = input("Are you sure you want to delete all tasks? (yes/no): ")
            confirm = confirm.strip().lower()  # Remove leading/trailing whitespace and convert to lowercase
            if confirm == "yes":
                tasks.clear()
                print("All tasks have been deleted.")
                save_tasks()  # Save the updated tasks list after clearing
            else:
                print("Operation cancelled.")
        case 11:
            completed_tasks = get_completed_tasks()
            pending_tasks = get_pending_tasks()
            if tasks:
                completion_rate = (len(completed_tasks) / len(tasks)) * 100
            else:
                completion_rate = 0.0
            print("Task Statistics:")
            print(f"Total tasks: {len(tasks)}")
            print(f"Pending tasks: {len(pending_tasks)}")
            print(f"Completed tasks: {len(completed_tasks)}")
            print(f"Completion rate: {completion_rate:.2f}%")

        case 12:
            print("Exiting the program...")
            break
        case _:
            print("Invalid option number, please try again")
    
        