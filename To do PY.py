import sys

# List to store tasks
tasks = []

def show_menu():
    print("\n--- To-Do List CLI ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else " "
            print(f"{index}. [{status}] {task['name']}")

def add_task():
    task_name = input("\nEnter task name: ")
    tasks.append({"name": task_name, "completed": False})
    print(f"Task '{task_name}' added!")

def mark_completed():
    view_tasks()
    try:
        task_num = int(input("\nEnter task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print(f"Task {task_num} marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("\nEnter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"Task '{deleted_task['name']}' deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice: ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("\nGoodbye!")
            sys.exit()
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()