from options.dump_fetch_tasks import load_tasks, save_tasks
import json

def add_tasks():
    print("How would you like to add tasks?")
    print("1. Import from JSON")
    print("2. Input manually")
    add_method=int(input())
    tasks=load_tasks() # Load existing tasks
    task={}
    
    while True:
        # If user chooses to import tasks from a JSON file
        if add_method == 1: 
            filename = input("Enter file's path: ")
            try:
                with open(filename, "r") as infile:
                    imported_tasks = json.load(infile)
                for task in imported_tasks:
                    task['status'] = "0"
                    tasks.append(task)
                task_counter = len(imported_tasks)
                print(task_counter, " tasks imported successfully!")
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
                task['description'] = task_name
                task['deadline'] = input("Task Deadline: ")
                task['priority'] = input("Task Priority (1-5): ")
                task['status'] = "0"
                tasks.append(task.copy())
                task = {}
                task_counter += 1
            break


        else:
            print("Invalid option selected. Please try again.")
            print("1. Import from JSON")
            print("2. Input manually")
            add_method = int(input("Input method (1 or 2): "))
    
    save_tasks(tasks)  # Save updated tasks
    print("Tasks added successfully!")