def todo_manager():
    todo_list = []
    print("=== Auspify Python Development Internship ===")
    print("--- Task 1: Personal To-Do List Application ---\n")
    
    while True:
        print("\n1. Add Task | 2. View Tasks | 3. Delete Task | 4. Exit")
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == '1':
            task = input("Enter the task description: ").strip()
            if task:
                todo_list.append(task)
                print(f"[SUCCESS] Added task: '{task}'")
            else:
                print("[ERROR] Task cannot be empty!")
                
        elif choice == '2':
            print("\n--- Current To-Do List ---")
            if not todo_list:
                print("No tasks found. Your list is empty!")
            else:
                for index, item in enumerate(todo_list, start=1):
                    print(f"{index}. {item}")
                    
        elif choice == '3':
            if not todo_list:
                print("[INFO] No tasks to delete.")
                continue
            print("\n--- Current To-Do List ---")
            for index, item in enumerate(todo_list, start=1):
                print(f"{index}. {item}")
            try:
                task_num = int(input("\nEnter task number to delete: "))
                if 1 <= task_num <= len(todo_list):
                    removed = todo_list.pop(task_num - 1)
                    print(f"[SUCCESS] Deleted task: '{removed}'")
                else:
                    print("[ERROR] Invalid task number!")
            except ValueError:
                print("[ERROR] Please enter a valid number.")
                
        elif choice == '4':
            print("\nExiting To-Do List Application. Thank you!")
            break
        else:
            print("[ERROR] Invalid input. Choose between 1-4.")

if __name__ == "__main__":
    todo_manager()
