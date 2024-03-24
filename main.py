from task import TaskManager
from utils import validate_index


def main():
    task_manager = TaskManager()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Update Task")
        print("4. List All Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)
        elif choice == '2':
            task_index = int(input("Enter task index to mark as completed: "))
            if validate_index(task_index, task_manager.tasks):
                task_manager.mark_task_completed(task_index)
        elif choice == '3':
            task_index = int(input("Enter task index to update: "))
            if validate_index(task_index, task_manager.tasks):
                title = input("Enter new task title: ")
                description = input("Enter new task description: ")
                task_manager.update_task(task_index, title, description)
        elif choice == '4':
            task_manager.list_tasks()
        elif choice == '5':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
