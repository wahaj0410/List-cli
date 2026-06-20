# List-cli
A little beginner code to list down stuff that needs to be done and marking it completed once done. Handy for keeping yourself organized!

## Features
- Add tasks
- List all tasks with completion status
- Mark tasks as complete
- Delete tasks
- Tasks persist between sessions via a local tasks.json file

## Tech stack
- Python 3
- Built-in json and os modules — no external dependencies

## How to run
1. Run locally
2. Clone the repo: git clone https://github.com/wahaj0410/List-cli.git
3. Navigate into the folder: cd List-cli
4. Run the app: python app.py  

## Usage
Once running, you'll see a menu:
1. List tasks
2. Add task
3. Complete task
4. Delete task
5. Exit
Type the number of the option you want and follow the prompts.

## Future improvements
- Add due dates and priority levels
- Add a .gitignore so tasks.json isn't tracked in git
- Add unit tests




import json
import os

    # tasks need to stay alive even after the program closes, we will use JSON and store them in a JSON file to do just that.
    TASKS_FILE = 'tasks.json'

    def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

    def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

    # Here we are adding tasks. Each task is a dictionary with an id, a title, and a done flag set to False by default.
    def add_task(tasks, title):
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {title}")

    # Here we are listing a task. It will loop through every task and prints a checkmark if done, a circle if not.
    def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "✔️" if task['done'] else "❌"
        print(f"{task['id']}. {status} {task['title']}")

    # Here we mark a task complete. 
    def complete_task(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            save_tasks(tasks)
            print(f"Task completed: {task['title']}")
            return
    print(f"Task with ID {task_id} not found.")
    
    # Here we delete tasks. 
    def delete_task(tasks, task_id):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            removed = tasks.pop(i)
            save_tasks(tasks)
            print(f"Task deleted: {removed['title']}")
            return
     print(f"Task with ID {task_id} not found.")
    
    # This the main menu, it is the entry point on the users end. It will keep the program running until the user quits.
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
    
    # The while True loop keeps showing the menu. The if __name__ == "__main__" block means this only runs when you execute the file directly.
