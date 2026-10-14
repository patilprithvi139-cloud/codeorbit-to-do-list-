tasks = []
def add_task():
    task = input("Enter your task: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")
def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour Tasks:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")
def remove_task():
    view_tasks()
    if not tasks:
        return
    try:
        number = int(input("Enter task number to remove: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
def main():
    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose (1-4): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("thank you for using to_do_list!")
            break
        else:
            print("Invalid choice. Choose 1-4.")
if __name__ == "__main__":
    main()