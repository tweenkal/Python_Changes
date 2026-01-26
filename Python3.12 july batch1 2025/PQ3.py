from datetime import datetime

# Example input
tasks = [
    {"task_id": 1, "task_name": "Write Report", "deadline": "2025-07-10",
     "priority": 2},
    {"task_id": 2, "task_name": "Code Review", "deadline": "2025-07-12",
     "priority": 3},
    {"task_id": 3, "task_name": "Update Database", "deadline": "2025-07-16",
     "priority": 1},
    {"task_id": 4, "task_name": "Test API", "deadline": "2025-07-14",
     "priority": 2}
]

current_date = "2025-07-15"

# Convert current_date to a datetime object
current = datetime.strptime(current_date, "%Y-%m-%d")

# Initialize lists and dictionary
overdue_tasks = []
priority_breakdown = {"Low": [], "Medium": [], "High": []}

# Priority mapping
priority_map = {1: "Low", 2: "Medium", 3: "High"}

# Process each task
for task in tasks:
    deadline_date = datetime.strptime(task["deadline"], "%Y-%m-%d")

    # Check overdue
    if deadline_date < current:
        overdue_tasks.append(task["task_name"])

    # Categorize by priority
    priority_name = priority_map[task["priority"]]
    priority_breakdown[priority_name].append(task["task_name"])

# Create final result
result = {
    "Overdue Tasks": overdue_tasks,
    "Priority Breakdown": priority_breakdown
}

# Display the result
print(result)
