from options.load_save_tasks import load_tasks, save_tasks
from options.view_tasks import display_tasks


def edit_task():
    display_tasks()

    task_id = int(input("Enter the ID of the task to edit: "))  
    description = input("Enter new description (leave blank to keep unchanged): ")
    deadline = input("Enter new deadline (leave blank to keep unchanged): ")
    priority = input("Enter new priority (leave blank to keep unchanged): ")

    tasks = load_tasks()
    for task in tasks:
        if task.get('id') == task_id:
            if description:
                task['description'] = description
            if deadline:
                task['deadline'] = deadline
            if priority:
                task['priority'] = priority
            save_tasks(tasks)
            print(f"Task {task_id} updated.")
            return
    print(f"Task {task_id} not found.")
    return

def mark_as_complete():
    display_tasks()
    
    task_id = int(input("Enter the ID of the task to mark as complete: "))
    tasks = load_tasks()
    for task in tasks:
        if task.get('id') == task_id:
            task['status'] = "1" if task.get('status') == "0" else "0"
            save_tasks(tasks)
            print(f"Task {task_id} marked as complete.")
            return
    print(f"Task {task_id} not found.")
    return
