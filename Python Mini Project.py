#Python Mini Project 


		
	
class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "Done" if self.completed else "Not Done"
        return f"{self.description} - {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for task in self.tasks:
            print(task)

    def mark_as_completed(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                task.completed = True
                print(f'Task "{task_description}" marked as completed.')
                return
        print(f'Task "{task_description}" not found.')

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.description},{task.completed}\n")

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                description, completed_str = line.strip().split(',')
                completed = True if completed_str == 'True' else False
                task = Task(description, completed)
                self.tasks.append(task)


def main():
    todo_list = ToDoList()

   
    try:
        todo_list.load_from_file('tasks.txt')
    except FileNotFoundError:
        pass

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Save and Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task_description = input("Enter task description: ")
            new_task = Task(task_description)
            todo_list.add_task(new_task)
        elif choice == '2':
            todo_list.display_tasks()
        elif choice == '3':
            task_description = input("Enter task description to mark as completed: ")
            todo_list.mark_as_completed(task_description)
        elif choice == '4':
            todo_list.save_to_file('tasks.txt')
            print("To-Do list saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()