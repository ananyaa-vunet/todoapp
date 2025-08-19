import json
import os
from dump_fetch_tasks import load_tasks, save_tasks
TASKS_FILE = 'tasks.json'


def edit_task(task_id, description=None, deadline=None, priority=None):
    tasks = load_tasks()
    for task in tasks:
        if task.get('id') == task_id:
            if description is not None:
                task['description'] = description
            if deadline is not None:
                task['deadline'] = deadline
            if priority is not None:
                task['priority'] = priority
            save_tasks(tasks)
            print(f"Task {task_id} updated.")
            return
    print(f"Task {task_id} not found.")
