# import datetime to use fuction to change date and os

from datetime import datetime as dt
import os

user_file = open("user.txt", "r+")

#**** login ****
# here we define login
# We will call login (variable) False as an boolen
# while login is equil to False user need to input username and password
# indented under the while loop we will create a for loop
# for line (variable) user_file will strip and split user_file (user.txt) and name each index [0] and [1] valid_user as 0 and valid_password as 1 on each line
# indented under the for loop if username is equal to valid_user and password is equal to valid_password. If they don't match up return username and details must be put in again
# if login is equal to False print statement incorrect details
# We use the seek(0) to reset the cursor to the begining of the user_file in user.txt each time username and password is insereted incorrectly.

def login():
    login = False

    while login == False:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for line in user_file:
            valid_user, valid_password = line.strip("\n").split(", ")

            if username == valid_user and password == valid_password:
                return username
        if login == False:
            print("Incorect details! Please enter a valid username and password")
        user_file.seek(0)

#**** Mani Menu ****
# Here we define main_menu
# menu will display as follow
# if username is equal to "admin" then we need to return back to menu as input file
# if username is not admin then return input menu by replacing gr,ds and r with nothing which will exclused those from the menu
def main_menu(username):
    menu = ("Please enter one of the following options:\nr - register user\na - add task\nva - view all tasks\n" +
            "vm - view my tasks\ngr - generate reports\nds - display statistics\ne - exit\n: ")

    if username == "admin":
        return input(menu)
    else:
        return input(menu.replace("gr - generate reports\n", "")
                     .replace("ds - display statistics\n", "")
                     .replace("r - register user\n", ""))

#**** Register user ****
# Here we define reg_user
# we will store run_register and found_user with True and False as boolen
# Now we will read and append out of user_file (user.txt)
# indented under user_file we will create a while loop for run_register
# for line (variable) user_file will strip and split user_file (user.txt) and name each index [0] and [1] valid_user as 0 and valid_password as 1 on each line
# indented under the for loop if username is equal to valid_user.strip()then if statement for found_user is True print user already exists.
# if not found_user we will then need to compair password with confirmed password and when they match only then will user_file write and append username and password to user.txt
# which run_register is False
# else print Password do not match for fiund_user
def reg_user():
    run_register = True
    found_user = False
    with open("user.txt", "a+") as user_file:
        while run_register:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user_file.seek(0)
            for line in user_file:
                valid_user, valid_password = line.strip("\n").split(", ")
                if username == valid_user.strip():
                    print("User already exists.")
                    found_user = True

            if not found_user:
                confirm = input("Please confirm password: ")
                if confirm == password:
                    print("Saving user")
                    user_file.write(f"\n{username}, {password}")
                    user_file.seek(0)
                    run_register = False
                else:
                    print("Passwords do not match. Try again")

#**** Add task ****
# Here we will read write and append
# the following variables are assiagned to each given input
# After user input data task_file write and append in a new file as task_file (task.txt) in the follong order f{}
# task_file.close() is used to close and save the new file that was created within task_file (tasks.txt)
def add_task():
    task_file = open("tasks.txt", "a+")

    task_name = input("Enter the username of the assigned task: ")
    title = input("Enter the title of the task: ")
    description = input("Enter the desription of the task: ")
    start_date = input("Enter the start date the task was assigned to user: ")
    end_date = input("Enter the end date the task was assigned to user: ")

    task_file.write(f"\n{task_name}, {title}, {description}, {start_date}, {end_date}, No")
    task_file.close()

#**** View All ****
# Here we will read only from tasks.txt
# for line (variable) in task_file (tasks.txt) we will assign a variables to each index when line (task_file in task.txt) is split by ", ".
# We will then display the following info using the f.{} when we assigned variable to the user.
def view_all():
    task_file = open("tasks.txt", "r")

    for line in task_file:
        task_name, title, description, start_date, end_date, is_completed = line.split(", ")

        print(f"""
        Username: {task_name}
        Title: {title}
        description = {description}
        Start date: {start_date}
        End date: {end_date}
        is_completed {is_completed}""")

#**** View mine ****
# Here we will read only from tasks.txt
# the name variable task_count = 0 so that we can count
# We will also create to emty list which we will use later to store inside the list (user_tasks = [] and task = [])
# for line (variable) in task_file (tasks.txt) we will assign a variables to each index when line (task_file in task.txt) is split by ", ".
# under the for loop for line (variable) if username is equal to task_name then user_tasks will append all info in line into a list
# The list in user_list will be counted using (task_count += 1)
# We will then display the following info using the f.{} when we assigned variable to the user.
# Take note that task_count is used to count
# if task_count is equal to 0 display to the user (You have no active task) and close task_file to save
# if task_count is not equal to 0 display amedn as (select a task to amend or press -1 to return)
# all_index will assign tasks.index(user_task[amedn])
# if amend is greater and equal to 0:
    # display choices
    # after that we will strip and split user_tasks and call in amend to edit input value(s)
    #We wil then create a boolen (modified)
    # if selected_task[5].lower() == "yes" display to the user Cannot modify as task is already complete
    # As long as is_completed is " no " the else statment will allow you to edit the following.
    # if u_choice is equal to 1 selected_task[5] = "yes" modified True
    # elif selected_task[0] = input("Enter the username: ")
    # Elif selected_task[3] = input("Enter the new due date: ")
    # if modified tasks[all_index] = ", ".join(selected_task) open("tasks.txt", "w").write("\n".join(tasks)) - here we will edit write join selected _task with task.txt

def view_mine(username):
    task_count = 0
    task_file = open("tasks.txt", "r")
    user_tasks = []
    tasks = []

    for line in task_file:
        task_name, title, description, start_date, end_date, is_completed = line.split(", ")
        tasks.append(line.strip())

        if username == task_name:
            user_tasks.append(line)
            task_count += 1

            print(f"""
            Task {task_count}) {title}
            \t- Username: {username}
            \t- description = {description}
            \t- Start date: {start_date}
            \t- End date: {end_date}
            \t- is_completed {is_completed}""")

    if task_count == 0:
        print("You have no active task")
        task_file.close()

    if task_count != 0:
        amend = int(input("Select a task to amend or press '-1' to return: ")) - 1
        all_index = tasks.index(user_tasks[amend])
        if amend >= 0:
            u_choice = input(
                "Select an option below:\n1 - Mark as complete\n2 - Change assignee\n3 - Change due date\n")
            selected_task = user_tasks[amend].strip().split(", ")
            modified = False
            if selected_task[5].lower() == "yes":
                print("Cannot modify already completed task.")
            else:
                if u_choice == "1":
                    selected_task[5] = "Yes"
                    modified = True
                elif u_choice == "2":
                    selected_task[0] = input("Enter the username: ")
                    modified = True
                elif u_choice == "3":
                    selected_task[3] = input("Enter the new due date: ")
                    modified = True
                else:
                    print("Invalid choice")

            if modified:
                tasks[all_index] = ", ".join(selected_task)
                open("tasks.txt", "w").write("\n".join(tasks))


def gen_task_overview():
    # Get all the tasks
    tasks = open("tasks.txt", "r").readlines()

    # Save the information needed
    total_tasks = len(tasks)
    tasks_completed = 0
    total_overdue_uncompleted = 0

    # Generate the task data
    for task in tasks:
        task_data = task.split(", ")
        # If the task is completed
        if task_data[-1] == "Yes":
            tasks_completed += 1
        # If the task is past its due date
        if dt.now() > dt.strptime(task_data[-3], "%d %b %Y"):
            total_overdue_uncompleted += 1

    # Store the task data in a dictionary
    task_overview = (f"Total Tasks: {total_tasks}\n"
                     f"Total completed tasks: {tasks_completed}\n"
                     f"Total uncompleted tasks: {total_tasks - tasks_completed}\n"
                     f"Total overdue and uncompleted: {total_overdue_uncompleted}\n"
                     f"Percentage incomplete: {(total_tasks - tasks_completed) / total_tasks * 100}\n"
                     f"Percentage completed: {tasks_completed / total_tasks * 100}\n")

    # Create the task content that gets written to the file
    open("task_overview.txt", "w").write(task_overview)


def gen_user_overview():
    # Get the users
    users = open("user.txt", "r").readlines()
    tasks = open("tasks.txt", "r").readlines()

    # Get the total amounts
    total_users = len(users)
    total_tasks = len(tasks)

    # Store the user data that will be written to the file
    data = [f"Total users: {total_users}", f"Total tasks: {total_tasks}"]

    # Get the user names and store in a list of users
    users = [line.split(", ")[0] for line in users]

    # for every user, get the amount of tasks, completed tasks, uncompleted tasks and overdue tasks
    for user in users:
        user_tasks = 0
        user_completed = 0
        user_uncompleted = 0
        user_overdue_uncompleted = 0
        # Count how many user_tasks, user_completed, user_uncompleted and user_overdue_uncompleted tasks there are
        for task in tasks:
            task_data = task.split(", ")
            # If the task belongs to the user get the appropriate information
            if task_data[0] == user:
                user_tasks += 1
                if task_data[-1] == "Yes":
                    user_completed += 1
                else:
                    user_uncompleted += 1
                if dt.now() > dt.strptime(task_data[-3], "%d %b %Y"):
                    user_overdue_uncompleted += 1
        if user_tasks > 0:
            content = ("_______________________________________\n"
                       f"User: {user}\n"
                       f"Total tasks: {user_tasks}\n"
                       f"Tasks owned: {user_tasks / total_tasks * 100}%\n"
                       f"Completed tasks: {user_completed / user_tasks * 100}%\n"
                       f"Uncompleted tasks: {user_uncompleted / user_tasks * 100}%\n"
                       f"Uncompleted and overdue: {user_overdue_uncompleted / user_tasks * 100}%")
        else:
            content = ("_______________________________________\n"
                       f"User: {user}\n"
                       f"Total tasks: {user_tasks}\n"
                       f"Tasks owned: {user_tasks / total_tasks * 100}%\n"
                       f"Completed tasks: 0%\n"
                       f"Uncompleted tasks: 0%\n"
                       f"Uncompleted and overdue: 0%")
        data.append(content)
        open("user_overview.txt", "w").write("\n".join(data))


def view_statistics():
    # If either of the files below do not exist, create them
    if not os.path.exists("user_overview.txt") or os.path.exists("task_overview.txt"):
        gen_task_overview()
        gen_user_overview()
    for line in open("user_overview.txt", "r").readlines():
        print(line.strip("\n"))
    for line in open("task_overview.txt", "r").readlines():
        print(line.strip("\n"))

# This is where we will run all our defintions
# we will create run_program is True and username is login() (define)
# We will create a loop
# while run_program
# selected_menu is main_menu(username) where we call into main_menu username
# if selected menu is equal to r use fuction reg_user the rest will be repeated
# by elif selected_menu is equal to gr then fuction gen_user_overview and gen_task_overview will take place
# by selecting e run_program will exit the loop because run_prgram is False
def run():
    run_program = True
    username = login()

    while run_program:
        selected_menu = main_menu(username)
        if selected_menu == "r":
            reg_user()
        elif selected_menu == "a":
            add_task()
        elif selected_menu == "va":
            view_all()
        elif selected_menu == "vm":
            view_mine(username)
        elif selected_menu == "gr":
            gen_user_overview()
            gen_task_overview()
        elif selected_menu == "ds":
            view_statistics()
        elif selected_menu == "e":
            print("Good bye")
            run_program = False
        else:
            print("Invalid input.")


run()
