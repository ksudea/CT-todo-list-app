'''
Global variables: predefined priorities and task completion status, and the task list which holds
our to do list!
'''

task_list = []
priorities = ["low", "medium", "high"]
statuses = ["Incomplete", "Complete"]

''' Made a custom class for tasks with title, status, and priority as attributes.
    Default status is incomplete, and default priority (bonus feature) is low.
'''
class Task:
  def __init__(self, title):
    self.title = title
    self.status = statuses[0]
    self.priority = priorities[0]


# Functions

def add_task(title):
    try:
        new_task = Task(title)
        task_list.append(new_task)
    except Exception as e:
       print(f"An error occurred: {e}")
    else:
       print("Task added to your list!")

def view_list():
    print("Here's your list:")
    print("Title:      Status:      Priority:  ")
    for task in task_list:
       print(task.title + "      " + task.status + "      " + task.priority)

def mark_complete(title):
    # find task with this title in our list
    title_found = False
    try:
        for t in task_list:
            if t.title == title:
                t.status = statuses[0]
                title_found = True
    except ValueError:
        print("There seems to be an error with the title you entered.")
    else:
        if title_found:
            print("Congrats! You finished this task!")
        else: 
           print("Sorry, this task doesn't exist in your to-do list. Try adding it first.")

# Bonus feature: priority of a task. There are 3 predefined priorities.
# this function changes priority of a task in our to-do list.   
def change_priority(title, priority_num):
    title_found = False
    try:
        new_priority = priorities[int(priority_num)]
        for t in task_list:
            if t.title == title:
                t.priority = new_priority
                title_found = True
    except (ValueError, TypeError):
        print("There seems to be an error with the title or priority you entered. \n Remember to enter an integer 0-2 as a priority.")
    else:
        if title_found:
            print(f"Priority updated! {title} priority is now {new_priority}")
        else: 
           print("Sorry, this task doesn't exist in your to-do list. Try adding it first.")

def delete_task(title):
    if len(task_list) == 0:
       print("Your list is already empty!")
       return
    title_found = False
    try:
       for t in task_list:
        if t.title == title:
          task_list.remove(t)
          title_found = True
    except ValueError:
        print("There seems to be an error with the title you entered.")
    else:
        if title_found:
            print("Task deleted.")
        else: 
           print("Sorry, this task doesn't seem to exist in your to-do list.")



if __name__ == '__main__':
 print("""Welcome to the To-Do List App!

                Menu:
                1. Add a task
                2. View tasks
                3. Mark a task as complete
                4. Change priority of a task
                5. Delete a task
                6. Quit
            """)
 
 run_program = True
 while run_program:
   try:
      action = int(input("Enter your choice (1-6):"))
      if action == 1:
        new_task_title = input("Enter the title of your new task!: ")
        add_task(new_task_title)
      elif action == 2:
        view_list()
      elif action == 3:
        task_title = input("Which task do you want to mark as complete?")
        mark_complete(task_title)
      elif action == 4: 
        print("""Priority options:
                0. low (default)
                1. medium
                2. high""")
        task_title = input("Which task do you want to change the priority of?")
        new_priority = input("Input new priority (numerical):")
        change_priority(task_title, new_priority)
      elif action == 5:
        task_title = input("Which task do you want to delete?")
        delete_task(task_title)
      elif action == 6:
        run_program = False
      else:
        print("Please enter an integer between 1-6 to make a choice on the menu.")
   except (ValueError, TypeError):
      print("Error! Remember, enter an integer between 1-6.")
   except Exception as e:
      print(f"An error occurred: {e}")
 print("Thanks for using the app!")