import json

def load_tasks():
    try:
        with open("tasks.json", "r") as infile:
            tasks = json.load(infile)
            return tasks
    except FileNotFoundError:
        print("No tasks exist.")
        return []
    except Exception as e:
        print("An error occurred while loading tasks:", e)
        return []
    
def save_tasks(tasks):
    try:
        with open("tasks.json", "w") as outfile:
            json.dump(tasks, outfile, indent=4)
    except Exception as e:
        print("An error occurred while saving tasks:", e)