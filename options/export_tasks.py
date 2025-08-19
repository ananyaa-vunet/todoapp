import json
from options.load_save_tasks import load_tasks


def export_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available to export.")
        return
    else:
        filename = input("Enter the filename to export tasks (default: 'exported_tasks.json'): ")+".json"
        if not filename:
            filename = "exported_tasks.json"
        try:
            with open(filename, "w") as outfile:
                json.dump(tasks, outfile, indent=4)
            print(f"Tasks successfully exported to {filename}.")
        except Exception as e:
            print(f"An error occurred while exporting tasks: {e}")
            return
