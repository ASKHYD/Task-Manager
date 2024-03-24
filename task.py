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

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            print("Task marked as completed!")
        else:
            print("Invalid task index.")

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
