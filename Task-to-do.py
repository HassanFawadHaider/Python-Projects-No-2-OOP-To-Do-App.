import json

class Task:
    def __init__(self, text, done=False):
        self.text = text
        self.done = done
  
    def mark_done(self):
        self.done = True
    

class Task_Manager(Task):
    def __init__(self):
        self.tasks = []
    #Helpers to load and save tasks from/to file
    def load_from_file(self):
        try:
            with open("Record.json", "r") as file:
                tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            tasks = []
    def save_to_file(self):
        with open("Record.json", "w") as file:
            json.dump([{"text": task.text, "done": task.done} for task in self.tasks], file, indent=4)   
            
    #----Features----
    #Add task
    def add_task(self, text):
        new_task = Task(text)          
        self.tasks.append(new_task)
        print("Task added:", text)
        self.save_to_file(self.tasks)


    #Show tasks
    def show_tasks(self):
        task_list = []
        try:
            self.load_from_file()
            for i, task in enumerate(task_list, start=1):
                status = "x" if task["done"] else " "
                print(f"{i}.[{status}] {task['text']}")
        except FileNotFoundError:
            print("No tasks found.")

    #Mark task as done
    def mark_task_done(self):
        task_list = []
        try:
            self.load_from_file()
            task_number = int(input("Enter the task number to mark as done:"))
            if 1 <= task_number <= len(task_list):
                task_list[task_number - 1]["done"] = True
                for i, task in enumerate(task_list, start=1):
                    status = "x" if task['done'] else " "
                    print(f"{i}.[{status}] {task['text']}")
            else:
                print("Invalid task number.")
            self.save_to_file()
        except ValueError:
            print("Please enter a valid number.")
        except FileNotFoundError:
            print("No tasks found.")

    #Delete task
    def delete_task(self):
        try:
            with open("Record.json", "r") as file:
                task_list = json.load(file)
            if not task_list:
                print("No tasks to delete.")
                return
            task_number = int(input("Enter the task number to delete:"))
            if 1 <= task_number <= len(task_list):
                del task_list[task_number - 1]
                for i, task in enumerate(task_list, start=1):
                    status = "x" if task['done'] else ""
                    print(f"{i}.[{status}] {task['text']}")
            else:
                print("Invalid task number.")
            with open("Record.json", "w") as file:
                json.dump(task_list, file, indent=4)
        except ValueError:
            print("Please enter a valid number.")
        except FileNotFoundError:
            print("No tasks found.")
    
app = Task_Manager()
print("Welcome to the Task Manager!")
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        task_text = input("Enter a new task: ")
        app.add_task(task_text)
    elif choice == '2':
        app.show_tasks()
    elif choice == '3':
        app.mark_task_done()
    elif choice == '4':
        app.delete_task()
    elif choice == '5':
        print("Exiting the Task Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")