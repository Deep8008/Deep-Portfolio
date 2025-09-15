import csv
import os


class Task:

    priority_order = {"very high": 4, "high": 3, "medium": 2, "low": 1}

    def __init__(self, job, description, priority):
        self.job = job
        self.description = description
        self.priority = priority.lower()

    def __str__(self):
        return f"Job: {self.job} - Desciption: {self.description} - Priority: {self.priority}"
    
    def __lt__(self, other):
        return Task.priority_order[self.priority] > Task.priority_order[other.priority]

### ToDoList ###
class ToDoList:
    def __init__(self):

        self.task_list = []
        
        config_file = os.path.join(os.path.dirname(__file__), "config.txt")

        if os.path.isfile(config_file):
            with open(config_file, "r") as f:
                path = f.read().strip()
        else:
            path = input("Enter full path for ToDoList CSV file (folder or file): ")
            with open(config_file, "w") as f:
                f.write(path)

        if os.path.isdir(path):
            path = os.path.join(path, "ToDoList_csv.csv")

        self.filename = path
        self.load_from_csv()


    def add_task(self, job, desc, prio):
        self.task_list.append(Task(job, desc, prio))
        self.task_list.sort()
        self.save_to_csv()
        
        print(f"You successfuly added ({job}) Job with ({prio}) Priority to your ToDoList!")
    
    def remove_task(self, job):
        found = False
        for task in self.task_list:
            if task.job == job:
                self.task_list.remove(task)
                found = True
                print("you successfuly removed ({job}) Task")
        if not found:
                print(f"No Task found with ({job}) Job")
        self.save_to_csv()

    def show_tasks(self):
        if not self.task_list:
            print("There is no Task here")
        else:
            for idx, task in enumerate(self.task_list, 1):
                print(f"{idx}. Job: {task.job} - Description: {task.description} - Priority: {task.priority}")

    def save_to_csv(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        with open(self.filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Job", "Description", "Priority"])
            for task in self.task_list:
                writer.writerow([task.job, task.description, task.priority])
    def load_from_csv(self):
        if os.path.isfile(self.filename) and os.path.getsize(self.filename) > 0:
            with open(self.filename, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    task = Task(row["Job"], row["Description"], row["Priority"])
                    self.task_list.append(task)
            self.task_list.sort()

### Menu ###
def show_menu():
    print("\nToDoList Menu:")
    print("1.Add Task")
    print("2.Remove Task")
    print("3.Show Tasks")
    print("4.Exit")

### Main ###
def main():
    todo = ToDoList()

    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            job = input("Enter task name: ")
            desc = input("Enter some description: ")
            print("Select Priority: 1.Low  2.Medium  3.High  4.Very High")
            prio_choice = input("Enter priority number: ")
            priority_map = {"1": "low", "2": "medium", "3": "high", "4": "very high"}
            prio = priority_map.get(prio_choice, "medium")
            todo.add_task(job, desc, prio)

        elif choice == "2":
            job = input("Enter task name: ")
            todo.remove_task(job)

        elif choice == "3":
            print("There is your Tasks:\n")
            todo.show_tasks()

        elif choice == "4":
            print("Exiting from ToDoList. Have a nice day!")
            break

        else:
            print("Invalid choice! Please select again.")


if __name__ == "__main__":
    main()

