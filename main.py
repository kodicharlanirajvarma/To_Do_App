from tasks import Task
from todo import ToDoManager
from storage import Storage

todo = ToDoManager()
storage = Storage()

todo.tasks = storage.load_tasks()

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
    print("8. Search task")
    print("9. Sort all tasks")
    print("10. Reopen a completed task")
    print("11. Delete all completed tasks")
    print("12. Delete all tasks")
    print("13. Check for overdue tasks")
    print("14. Task statistics")
    print("15. Exit")
    try:
        choice = int(input("Enter your option number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    match choice:
        case 1:
            task = input("Enter your task to add: ")
            priority = input("Enter the task priority: ")
            due_date = input("Enter the due date of your task: ")
            todo.add_task(task, priority, due_date)
            storage.save(todo.tasks)
        case 2:
            todo.show_tasks()
        case 3:
            todo.view_completed()
        case 4:
            todo.show_tasks()
        case 5:
            index = int(input("Enter your task number you want to remove: "))
            todo.remove_task(index-1)
            storage.save(todo.tasks)
        case 6:
            index = int(input("Enter the task number you want to complete: "))
            todo.complete_tasks(index-1)
            storage.save(todo.tasks)
        case 7:
            todo.show_tasks()
            index = int(input("Enter the task number you want to edit: "))
            new_task = input("Enter the new task: ")
            todo.edit_task(index-1, new_task)
            storage.save(todo.tasks)
        case 8:
            title = input("Enter the task to search: ")
            todo.search_task(title)
        case 9:
            print("1. Sort according to priority")
            print("2. Sort according to Due date")
            try:
                decision = int(input("Enter your choice: "))
                match decision:
                    case 1:
                        todo.sort_by_priority()
                    case 2:
                        todo.sort_by_due_date()
                    case _:
                        print("Enter a valid number")
            except ValueError:
                print("Enter a number")
        case 10:
            index = int(input("Enter the task number you want to reopen: "))
            todo.reopen_task(index-1)
            storage.save(todo.tasks)
        case 11:
            todo.delete_all_completed_tasks()
            storage.save(todo.tasks)
        case 12:
            todo.delete_all_tasks()
            storage.save(todo.tasks)
        case 13:
            todo.overdue_tasks()
        case 14:
            todo.task_statistics()
        case 15:
            print("Exiting the program...")
            break
        case _:
            print("Invalid option number, please try again")
    
        