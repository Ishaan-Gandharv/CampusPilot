
import json
from datetime import datetime

FILE_NAME = "tasks.json"


def load_tasks():
    """Load saved assignments from the file."""
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: Task file is invalid. Starting empty.")
        return []


def save_tasks(tasks):
    """Save assignments to a file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Assignment name: ").strip()

    if not title:
        print("Assignment name cannot be empty.")
        return

    due_date = input("Due date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.")
        return

    print("Priority: 1. High  2. Medium  3. Low")
    choice = input("Choose priority: ").strip()

    priorities = {
        "1": "High",
        "2": "Medium",
        "3": "Low"
    }

    if choice not in priorities:
        print("Invalid priority.")
        return

    task = {
        "title": title,
        "due_date": due_date,
        "priority": priorities[choice],
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Assignment added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No assignments found.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(f"\n{index}. {task['title']}")
        print(f"   Due: {task['due_date']}")
        print(f"   Priority: {task['priority']}")
        print(f"   Status: {status}")


def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter assignment number to complete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if 1 <= number <= len(tasks):
        tasks[number - 1]["completed"] = True
        save_tasks(tasks)
        print("Assignment marked as completed!")
    else:
        print("Assignment number does not exist.")


def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter assignment number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if 1 <= number <= len(tasks):
        removed = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['title']}")
    else:
        print("Assignment number does not exist.")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== CampusPilot =====")
        print("1. Add assignment")
        print("2. View assignments")
        print("3. Complete assignment")
        print("4. Delete assignment")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Thank you for using CampusPilot!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
