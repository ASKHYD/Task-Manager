# Given the existing structure of the TaskManager class, here is an update that allows
# tasks to be marked completed by name.

class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print("Task added successfully!")

    def mark_task_completed_by_name(self, task_name):
        # Search for the task by name
        for task in self.tasks:
            if task.title == task_name:
                task.completed = True
                print(f"Task '{task_name}' marked as completed!")
                return
        # If not found, print an error message
        print(f"Task with name '{task_name}' not found.")

    def update_task(self, task_index, title, description):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].title = title
            self.tasks[task_index].description = description
            print("Task updated successfully!")
        else:
            print("Invalid task index.")

    def list_tasks(self):
        print("Task List:")
        for index, task in enumerate(self.tasks):
            status = "Completed" if task.completed else "Pending"
            print(f"{index}: {task.title} - {task.description} ({status})")

# Updating the main function to allow marking tasks completed by name
def main():
    task_manager = TaskManager()
    
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Mark Task as Completed by Name")
        print("3. Update Task")
        print("4. List All Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)
        elif choice == '2':
            task_name = input("Enter task name to mark as completed: ")
            task_manager.mark_task_completed_by_name(task_name)
        elif choice == '3':
            task_index = int(input("Enter task index to update: "))
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
