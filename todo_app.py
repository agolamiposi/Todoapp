# todo_app.py

# Load tasks from the text file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.read().splitlines()
        return tasks
    except FileNotFoundError:
        return []

# Save tasks to the text file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Main function to run the application
def main():
    print("Text-Based To-Do List Application\n")

    tasks = load_tasks()

    while True:
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

        elif choice == "2":
            new_task = input("Enter the new task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("Task added successfully!")

        elif choice == "3":
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            try:
                task_index = int(input("Enter the task number to mark as completed: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks.pop(task_index)
                    save_tasks(tasks)
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
