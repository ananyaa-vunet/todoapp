from options.load_save_tasks import load_tasks, save_tasks

def delete_task():
    task_id = input("Enter the ID of the task to delete: ")
    tasks = load_tasks()
    task_found = False
    for task in tasks:
        if str(task.get('id')) == str(task_id):
            tasks.remove(task)
            task_found = True
            break
    if task_found:
        save_tasks(tasks)
        print(f"Task {task_id} deleted successfully.")
    else:
        print(f"Task {task_id} not found.")
    return