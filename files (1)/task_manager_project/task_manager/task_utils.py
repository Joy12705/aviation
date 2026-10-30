from datetime import datetime

# Import validation functions
from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)

# Define tasks list (each task is a dictionary)
tasks = []


# Implement add_task function
def add_task(title, description, due_date):
    """Validate the input and, if valid, append a new task. Returns True/False."""
    if not (validate_task_title(title)
            and validate_task_description(description)
            and validate_due_date(due_date)):
        print("Task was not added.")
        return False

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False,
    }
    tasks.append(task)
    print("Task added successfully!")
    return True


# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    """Mark the task at the given (0-based) list index as complete. Returns True/False."""
    if not isinstance(index, int) or isinstance(index, bool) or not 0 <= index < len(tasks):
        print("Error: Invalid task number.")
        return False
    if tasks[index]["completed"]:
        print("That task is already complete.")
        return False
    tasks[index]["completed"] = True
    print("Task marked as complete!")
    return True


# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    """Print all tasks that are not complete. Task numbers are 1-based. Returns the pending tasks."""
    pending = [(i, t) for i, t in enumerate(tasks) if not t["completed"]]
    if not pending:
        print("No pending tasks.")
        return []
    print("Pending Tasks:")
    for i, t in pending:
        print(f"{i + 1}. {t['title']} - {t['description']} (Due: {t['due_date']})")
    return [t for _, t in pending]


# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    """Return the percentage (0-100) of tasks that are complete; 0.0 if there are no tasks."""
    if not tasks:
        progress = 0.0
    else:
        completed = sum(1 for t in tasks if t["completed"])
        progress = completed / len(tasks) * 100
    return progress
