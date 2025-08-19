from options.load_save_tasks import load_tasks, save_tasks
import json

def add_tasks():
    print("How would you like to add tasks?")
    print("1. Import from JSON")
    print("2. Input manually")
    while True:
        add_method_input = input()
        if add_method_input.isdigit() and int(add_method_input) in [1, 2]:
            add_method = int(add_method_input)
            break
        else:
            print("Invalid input. Please enter 1 or 2.")
    tasks = load_tasks()  # Load existing tasks

    # Find the next available ID
    if tasks:
        next_id = max(int(task.get('id', 0)) for task in tasks) + 1
    else:
        next_id = 1

    task = {}

    while True:
        # If user chooses to import tasks from a JSON file
        if add_method == 1:
            filename = input("Enter file's path: ")
            try:
                with open(filename, "r") as infile:
                    imported_tasks = json.load(infile)
                for imported_task in imported_tasks:
                    imported_task['id'] = next_id
                    imported_task['status'] = "0"
                    tasks.append(imported_task)
                    next_id += 1
                print(len(imported_tasks), " tasks imported successfully!")
                break
            except Exception as e:
                print("Error reading file:", e)
                return

        # If user chooses to input tasks manually
        elif add_method == 2:
            task_counter = 1
            while True:
                print("Enter details for Task", task_counter, "(or type 'exit' to finish):")
                task_name = input("Task Description: ")
                if task_name.lower() == 'exit':
                    break
                task['id'] = next_id
                task['description'] = task_name
                task['deadline'] = input("Task Deadline (DD-MM-YY): ")
                task['priority'] = input("Task Priority (1-5): ")
                task['status'] = "0"
                tasks.append(task.copy())
                task = {}
                next_id += 1
                task_counter += 1
            break

        else:
            print("Invalid option selected. Please try again.")
            print("1. Import from JSON")
            print("2. Input manually")
            add_method = int(input("Input method (1 or 2): "))

    save_tasks(tasks)  # Save updated tasks
    print("Tasks added successfully!")