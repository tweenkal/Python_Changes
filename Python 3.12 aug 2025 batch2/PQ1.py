"""
Task Management System
Allows user to add tasks, search, list pending tasks, view details, and mark tasks completed.
"""

class Task:
    """Represents a single task in the system."""
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        """Mark this task as completed."""
        self.completed = True

    def display_task(self):
        """Display detailed information about the task."""
        status = "Completed" if self.completed else "Pending"
        print(f"Title      : {self.title}")
        print(f"Description: {self.description}")
        print(f"Priority   : {self.priority}")
        print(f"Status     : {status}")
        print("-" * 30)


# List to store all tasks
task_list = []

while True:
    print("\n--- Task Management System ---")
    print("1. Add Task")
    print("2. Search Task")
    print("3. List Pending Tasks")
    print("4. Display Task Details")
    print("5. Mark Task Completed")
    print("6. Exit")

    user_choice = input("Enter your choice (1-6): ")

    if user_choice == "1":
        task_title = input("Enter task title: ")
        task_description = input("Enter task description: ")
        task_priority = input("Enter task priority (Low/Medium/High): ")
        new_task = Task(task_title, task_description, task_priority)
        task_list.append(new_task)
        print(f"Task '{task_title}' added successfully!\n")

    elif user_choice == "2":
        search_type = input("Search by title or priority? ").lower()
        if search_type in ["title", "priority"]:
            search_value = input(f"Enter {search_type}: ")
            found_tasks = []
            if search_type == "title":
                found_tasks = [task for task in task_list if search_value.lower() in task.title.lower()]
            else:
                found_tasks = [task for task in task_list if task.priority.lower() == search_value.lower()]

            if found_tasks:
                print(f"Found {len(found_tasks)} task(s):")
                for task in found_tasks:
                    task.display_task()
            else:
                print("No tasks found!\n")
        else:
            print("Invalid search type.\n")

    elif user_choice == "3":
        pending_tasks = [task for task in task_list if not task.completed]
        if pending_tasks:
            print("Pending tasks:")
            for task in pending_tasks:
                task.display_task()
        else:
            print("No pending tasks!\n")

    elif user_choice == "4":
        detail_title = input("Enter task title to view details: ")
        for task in task_list:
            if task.title.lower() == detail_title.lower():
                task.display_task()
                break
        else:
            print("Task not found!\n")

    elif user_choice == "5":
        complete_title = input("Enter task title to mark as completed: ")
        for task in task_list:
            if task.title.lower() == complete_title.lower():
                task.mark_completed()
                print(f"Task '{complete_title}' marked as completed.\n")
                break
        else:
            print("Task not found!\n")

    elif user_choice == "6":
        print("Exiting Task Management System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.\n")
