import json
import maskpass
from options.add_tasks import add_tasks
from options.edit_task import edit_task, mark_as_complete
from options.delete_task import delete_task
from options.view_tasks import display_tasks, sort_tasks_by_date, sort_tasks_by_priority
from options.export_tasks import export_tasks


def print_header(title):
    print(f"\n{title}")
    print("_" * 25)

def main_menu():
    while True:
        print("\nMain Menu:")
        print("0. Exit")
        print("1. Create tasks")
        print("2. Change status of tasks")
        print("3. Edit tasks")
        print("4. Delete tasks")
        print("5. View tasks")
        print("6. Bulk export tasks as JSON")
        action = input("Select an option (0-6): ")
        if not action.isdigit():
            print("Invalid option selected. Please try again.")
            continue
        action = int(action)

        if action == 0: # Exit option
            print_header("Exit")
            print("Thank you for using To-Do App!")
            print("Exiting the application.")
            break


        elif action == 1: # Create tasks option
            print_header("Create Tasks")
            add_tasks()


        elif action == 2:# Change status of tasks option
            print_header("Change Status of Tasks")
            mark_as_complete()

        
        elif action == 3: # Edit tasks option
            print_header("Edit Tasks")
            edit_task()


        elif action == 4: # Delete tasks option
            print_header("Delete Tasks")
            delete_task()


        elif action == 5: # View tasks option
            print_header("View Tasks")
            print("How would you like to view tasks?")
            print("1. View all tasks")
            print("2. Sort tasks by date")
            print("3. Sort tasks by priority")
            while True:
                view_option = input("Select an option (1-3): ")
                if not view_option.isdigit():
                    print("Invalid option selected. Please enter a number between 1 and 3.")
                    continue
                if view_option == '1': # View all tasks option
                    print_header("View All Tasks")
                    display_tasks()
                    break
                elif view_option == '2': # Sort tasks by date option
                    print_header("Sort Tasks by Date")
                    sort_tasks_by_date()
                    break
                elif view_option == '3': # Sort tasks by priority option
                    print_header("Sort Tasks by Priority")
                    sort_tasks_by_priority()
                    break
                else: # Invalid option
                    print("Invalid option selected. Please try again.")


        elif action == 6: # Bulk export tasks as JSON option
            print_header("Bulk Export Tasks as JSON")
            export_tasks()


        else: # Invalid option
            print("Invalid option selected. Please try again.")


if __name__ == '__main__':
    print("Welcome to To-Do App")
    print("Login to continue: ")
    username = input("Username: ")
    password = maskpass.askpass(prompt="Password:", mask="*")
    while username != "user1" or password != "user1":
        print("Invalid Credentials, Try Again")
        username = input("Username: ")
        password = maskpass.askpass(prompt="Password:", mask="*")
    else:
        main_menu() # If credentials are valid, proceed to main menu