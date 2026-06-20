import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks, title):
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {title}")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "✔️" if task['done'] else "❌"
        print(f"{task['id']}. {status} {task['title']}")

def complete_task(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            save_tasks(tasks)
            print(f"Task completed: {task['title']}")
            return
    print(f"Task with ID {task_id} not found.")

def delete_task(tasks, task_id):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            removed = tasks.pop(i)
            save_tasks(tasks)
            print(f"Task deleted: {removed['title']}")
            return
    print(f"Task with ID {task_id} not found.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List: ---")
        print("1. List tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("\nChoose an option: ").strip()

        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            title = input("Enter task title: ").strip()
            if title:
                add_task(tasks, title)
        elif choice == '3':
            task_id = int(input("Enter task ID to complete: "))
            complete_task(tasks, task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(tasks, task_id)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()