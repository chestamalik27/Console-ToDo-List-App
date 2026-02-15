# Simple To-Do List App (No Functions)

file_name = "tasks.txt"

# Load existing tasks
try:
    with open(file_name, "r") as f:
        tasks = f.read().splitlines()
except:
    tasks = []

while True:
    print("==== TO-DO MENU ====")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Update Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if len(tasks) == 0:
            print("\nNo tasks yet.\n")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
            print()

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        with open(file_name, "w") as f:
            for t in tasks:
                f.write(t + "\n")
        print("Task added!\n")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.\n")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
            try:
                num = int(input("Enter task number to remove: "))
                removed = tasks.pop(num - 1)
                with open(file_name, "w") as f:
                    for t in tasks:
                        f.write(t + "\n")
                print(f"Removed: {removed}\n")
            except:
                print("Invalid input.\n")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to update.\n")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
            try:
                num = int(input("Enter task number to update: "))
                new_task = input("Enter updated task: ")
                tasks[num - 1] = new_task
                with open(file_name, "w") as f:
                    for t in tasks:
                        f.write(t + "\n")
                print("Task updated!\n")
            except:
                print("Invalid input.\n")

    elif choice == "5":
        print("Goodbye 👋")
        break

    else:
        print("Please choose a valid option.\n")