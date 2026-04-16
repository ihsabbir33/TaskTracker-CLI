import argparse
import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"

# Colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"


# Load tasks (FIXED)
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Generate unique ID
def generate_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


# Add task
def add_task(description):
    tasks = load_tasks()

    new_task = {
        "id": generate_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print(f"{GREEN}✅ Task added successfully (ID: {new_task['id']}){RESET}")


# Update task
def update_task(task_id, description):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f"{GREEN}✅ Task updated successfully{RESET}")
            return

    print(f"{RED}❌ Task not found{RESET}")


# Delete task
def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]

    if len(tasks) == len(new_tasks):
        print(f"{RED}❌ Task not found{RESET}")
        return

    save_tasks(new_tasks)
    print(f"{GREEN}✅ Task deleted successfully{RESET}")


# Mark status
def mark_status(task_id, status):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f"{GREEN}✅ Task marked as {status}{RESET}")
            return

    print(f"{RED}❌ Task not found{RESET}")


# List tasks (table format)
def list_tasks(filter_status=None):
    tasks = load_tasks()

    if filter_status:
        tasks = [task for task in tasks if task["status"] == filter_status]

    if not tasks:
        print(f"{YELLOW}⚠️ No tasks found{RESET}")
        return

    print("\n📋 Tasks:")
    print("-" * 60)
    print(f"{'ID':<5}{'Description':<25}{'Status':<15}")
    print("-" * 60)

    for task in tasks:
        print(f"{task['id']:<5}{task['description']:<25}{task['status']:<15}")

    print("-" * 60)


# Main CLI
def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--desc", required=True)

    # Update
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("--id", type=int, required=True)
    update_parser.add_argument("--desc", required=True)

    # Delete
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", type=int, required=True)

    # Mark in progress
    in_progress_parser = subparsers.add_parser("mark-in-progress")
    in_progress_parser.add_argument("--id", type=int, required=True)

    # Mark done
    done_parser = subparsers.add_parser("mark-done")
    done_parser.add_argument("--id", type=int, required=True)

    # List
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--status", required=False)

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.desc)

    elif args.command == "update":
        update_task(args.id, args.desc)

    elif args.command == "delete":
        delete_task(args.id)

    elif args.command == "mark-in-progress":
        mark_status(args.id, "in-progress")

    elif args.command == "mark-done":
        mark_status(args.id, "done")

    elif args.command == "list":
        list_tasks(args.status)


if __name__ == "__main__":
    main()