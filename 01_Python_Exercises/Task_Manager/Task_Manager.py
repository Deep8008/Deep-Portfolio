import sqlite3
import os

class Task_Manager():
    def __init__(self, db_path):
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()

        self.cur.execute('''CREATE TABLE IF NOT EXISTS tasks(
                         id INTEGER PRIMARY KEY,
                         title TEXT,
                         description TEXT,
                         priority TEXT,
                         status TEXT DEFAULT 'pending',
                         deadline TEXT,
                         last_updated TEXT DEFAULT CURRENT_TIMESTAMP
                         )''')
        self.con.commit()
    
    def add_task(self, title, description, priority, deadline):
        self.cur.execute('''INSERT INTO tasks(
                         title,
                         description,
                         priority,
                         deadline
                         ) VALUES(?,?,?,?)''', (title, description, priority, deadline))
        self.con.commit()
        print("Task added succsessfuly")

    def show_tasks(self):
        self.cur.execute('''SELECT * FROM tasks
                         ORDER BY last_updated ASC
                         ''')
        tasks = self.cur.fetchall()
        if not tasks:
            print("There is no task here.")
        else:
            for task in tasks:
                print(task)
    
    def show_pending(self):
        self.cur.execute('''SELECT * FROM tasks WHERE status = 'pending'
                         ''')
        tasks = self.cur.fetchall()
        if not tasks:
            print("There is no pending task here.")
        else:
            for task in tasks:
                print(task)
    
    def update_status(self, task_id, new_status):
        self.cur.execute('SELECT * FROM tasks WHERE id=?', (task_id,))
        task = self.cur.fetchone()
        if not task:
            print("This task does not exist.")
            return
    
        self.cur.execute('''UPDATE tasks
                         SET status = ?, last_updated = CURRENT_TIMESTAMP
                         WHERE id = ?
                         ''', (new_status, task_id))
        self.con.commit()
        print(f"Task ({task_id}) updated successfully.")

    def delete_task(self, task_id):
        self.cur.execute('''SELECT * FROM tasks WHERE id=?
                         ''', (task_id))
        task = self.cur.fetchone()
        if not task:
            print("This task does not exist.")
            return
    
        self.cur.execute('''DELETE FROM tasks WHERE id = ?
                         ''', (task_id))
        self.con.commit()
        print(f"Task ({task_id}) deleted successfully.")

    def show_summary(self):
        self.cur.execute('''SELECT COUNT(*) FROM tasks
                         ''')
        total = self.cur.fetchone()[0]

        if total == 0:
            print("There is no task here.")
            return

        self.cur.execute('''SELECT COUNT(*) FROM tasks WHERE status = 'done'
                         ''')
        done = self.cur.fetchone()[0]

        pending = total - done

        progress = (done / total) * 100 if total > 0 else 0

        print(f"Total: {total}\nDone: {done}\nPending: {pending}\nProgress: {progress:.1f}%")
    
    def close_table(self):
        self.con.close()
    

def menu():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "my_database.db")
    my_db = Task_Manager(db_path)

    while True:
        print("\n1. Add Task\n2. Show Tasks\n3. Show Pendings\n4. Update Task\n5. Delete Task\n6. Summary\n7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the task Title: ")
            description = input("Enter the task Description: ")
            priority = input("Enter the task Priority: ")
            deadline = input("Enter the task Deadline: ")
            my_db.add_task(title, description, priority, deadline)

        elif choice == "2":
            my_db.show_tasks()

        elif choice == "3":
            my_db.show_pending()
        
        elif choice == "4":
            task_id = input("Enter the task ID: ")
            my_db.update_status(task_id, "done")

        elif choice == "5":
            task_id = input("Enter the task ID: ")
            my_db.delete_task(task_id)

        elif choice == "6":
            my_db.show_summary()

        elif choice == "7":
            print("Exiting the program...\nGood Luck!")
            break
        
        else:
            print("Invalid choice!, please select a valid choice.")
    
    my_db.close_table()


if __name__ == "__main__":
    menu()
