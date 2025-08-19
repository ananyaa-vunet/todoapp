import json
import os

def delete_task(task_id, file_path='tasks.json'):
    if not os.path.exists(file_path):
        return False

    with open(file_path, 'r') as f:
        try:
            tasks = json.load(f)
        except json.JSONDecodeError:
            return False

    new_tasks = [task for task in tasks if task.get('id') != task_id]

    if len(new_tasks) == len(tasks):
        return False  # Task not found

    with open(file_path, 'w') as f:
        json.dump(new_tasks, f, indent=4)

    return True