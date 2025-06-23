import argparse
import json
import os

# Define the file where tasks will be stored
TASKS_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from the JSON file. Returns an empty list if the file doesn't exist."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    """Saves the list of tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(task_description):
    """Adds a new task to the list."""
    tasks = load_tasks()
    tasks.append({"description": task_description, "status": "pending"})
    save_tasks(tasks)
    print(f"Added task: '{task_description}'")

def list_tasks():
    """Lists all tasks with their ID and status."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    
    print("\n--- To-Do List ---")
    for idx, task in enumerate(tasks):
        print(f"{idx + 1}. [{task['status']}] {task['description']}")
    print("------------------\n")

def complete_task(task_id):
    """Marks a task as complete."""
    tasks = load_tasks()
    if 0 < task_id <= len(tasks):
        tasks[task_id - 1]["status"] = "complete"
        save_tasks(tasks)
        print(f"Task {task_id} marked as complete.")
    else:
        print("Error: Invalid task ID.")

def main():
    """Main function to parse arguments and call appropriate functions."""
    parser = argparse.ArgumentParser(description="A simple command-line to-do list manager.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 'add' command
    add_parser = subparsers.add_parser("add", help="Add a new task.")
    add_parser.add_argument("description", type=str, help="The description of the task.")

    # 'list' command
    subparsers.add_parser("list", help="List all tasks.")

    # 'done' command
    done_parser = subparsers.add_parser("done", help="Mark a task as complete.")
    done_parser.add_argument("id", type=int, help="The ID of the task to complete.")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        complete_task(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
