import json
import maskpass
from options.add_tasks import add_tasks, load_tasks


def main_menu():
    while True:
        print("\nSelect your option:")
        print("0. Exit")
        print("1. Create tasks")
        action = input()
        if not action.isdigit():
            print("Invalid option selected. Please try again.")
            continue
        action = int(action)
        if action == 0:
            print("Thank you for using To-Do App!")
            print("Exiting the application.")
            break
        elif action == 1:
            add_tasks()
        else:
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
        main_menu()