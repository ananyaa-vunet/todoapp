from datetime import datetime
from options.load_save_tasks import load_tasks

# Unicode symbols
TICK = "\u2713"      # ✓
BOX = "\u2610"       # ☐


def calculate_column_widths(tasks):
    id_width = max(max(len(str(task.get('id', ''))) for task in tasks), len("ID"))
    desc_width = max(max(len(task.get('description', '')) for task in tasks), len("Description"))
    deadline_width = max(max(len(task.get('deadline', '')) for task in tasks), len("Deadline"))
    priority_width = max(max(len(str(task.get('priority', ''))) for task in tasks), len("Priority"))
    status_width = len("Status")
    return id_width, desc_width, deadline_width, priority_width, status_width

def display_tasks(tasks=None):
    if tasks is None:
        tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return

    id_width, desc_width, deadline_width, priority_width, status_width = calculate_column_widths(tasks)

    # Print header
    print("-" * (id_width + desc_width + deadline_width + priority_width + status_width + 13))
    print(f"{'ID':^{id_width}} | {'Description':^{desc_width}} | {'Deadline':^{deadline_width}} | {'Priority':^{priority_width}} | {'Status':^{status_width}}")
    print("-" * (id_width + desc_width + deadline_width + priority_width + status_width + 13))

    # Print tasks

    for task in tasks:
        task_id = str(task.get('id', ''))
        description = task.get('description', '')
        deadline = task.get('deadline', '')
        priority = str(task.get('priority', ''))
        status = TICK if task.get('status', '0') == "1" else BOX

        print(f"{task_id:<{id_width}} | {description:<{desc_width}} | {deadline:<{deadline_width}} | {priority:<{priority_width}} | {status:<{status_width}}")
    print("-" * (id_width + desc_width + deadline_width + priority_width + status_width + 13))



def sort_tasks_by_date():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return
    display_tasks(sorted(tasks, key=lambda t: datetime.strptime(t.get('deadline', '31-12-9999'), "%d-%m-%Y")))
    return

def sort_tasks_by_priority():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return
    display_tasks(sorted(tasks, key=lambda t: t.get('priority', 0), reverse=False))
    return