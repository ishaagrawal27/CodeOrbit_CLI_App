
# To-Do List CLI App
# This program allows users to add, view, and remove tasks.

# Predefined list of tasks
tasks = [
    "Complete Python internship assignment",
    "Practice Python programming",
    "Prepare project README file",
    "Upload project to GitHub",
    "Review internship feedback"
]


# Function to display all tasks
def view_tasks():
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\n===== YOUR TO-DO LIST =====")
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")


# Function to add a new task
def add_task():
    task = input("Enter a new task: ").strip()

    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


# Function to remove a task
def remove_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter the task number to remove: "))

        if 1 <= number <= len(tasks):
            removed_task = tasks.pop(number - 1)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# Main function to run the application
def main():
    while True:
        print("\n===== TO-DO LIST APP =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Thank you for using the To-Do List App!")
            break
        else:
            print("Invalid choice. Please select 1 to 4.")


# Start the program
if __name__ == "__main__":
    main()
