from datetime import datetime

MAX_TITLE_LENGTH = 100
MAX_DESCRIPTION_LENGTH = 500


def validate_task_title(title):
    """Return True if the title is a non-empty string of at most 100 characters."""
    if not isinstance(title, str) or not title.strip():
        print("Error: Task title cannot be empty.")
        return False
    if len(title.strip()) > MAX_TITLE_LENGTH:
        print(f"Error: Task title cannot be longer than {MAX_TITLE_LENGTH} characters.")
        return False
    return True


def validate_task_description(description):
    """Return True if the description is a non-empty string of at most 500 characters."""
    if not isinstance(description, str) or not description.strip():
        print("Error: Task description cannot be empty.")
        return False
    if len(description.strip()) > MAX_DESCRIPTION_LENGTH:
        print(f"Error: Task description cannot be longer than {MAX_DESCRIPTION_LENGTH} characters.")
        return False
    return True


def validate_due_date(due_date):
    """Return True if due_date is a real calendar date written as YYYY-MM-DD."""
    if not isinstance(due_date, str):
        print("Error: Due date must be text in the format YYYY-MM-DD.")
        return False
    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
    except ValueError:
        print("Error: Invalid due date. Use the format YYYY-MM-DD (for example 2024-06-26).")
        return False
    return True
