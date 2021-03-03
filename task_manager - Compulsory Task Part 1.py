
#********* login *********

# Here we will read and write file in 'user.txt'
# We will then create a variable 'login' as boolen for later use
user_file = open("user.txt","r+")
login = False


# while login is equil to False username and password will be printed out to be entered by the user:
while login == False:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
# indented under while loop line 11
# for loop, line (variable) in user_file (the file in user.txt)
# here will will assign valid_user and valid_password to the text in user_file by making use of unpacking and splitting by a comma in user_file
# if statement indented under for loop
# if username entered by user is equal to valid_user in user_file the same for password then login is true and will display menu.    
    for line in user_file:
        valid_user, valid_password = line.strip("\n").split(", ") # need to strip away the new line "\n" when user input a new register user (otherwise login don't work)

        if username == valid_user and password == valid_password:
            login = True
# If above is not true below will be false and message will be printed out then string will be looped by the while loop to enter correct username and password again.
# user_file.seek(0) is used to seek for the correct username and password as cursor moves along from left to right looking for a match
    if login == False:
        print("Incorect details! Please enter a valid username and password")
    user_file.seek(0)

#********* Menu for normal user *********

# menu below will be printed out
if username != "admin":
    choice = input("""
    Please select one of the following options:
    r - register user
    a - add task
    va - view al tasks
    vm - view my tasks
    e - exit
    """)
#********* admin menu *********
#********* choice "s" for admin *********
    #$$$$ check speudo

# When user enter "s"
# choice 's' is indented and nested under the admin menu other users won't be able to access if you not admin
# indented by under the if statement in line 35 so that the menu can follow a set of rules
# if user choose "s" the following will take place indented under if for statement
# task_file and user_file will be opened and be read only "r"
# for line in task_file the following will be assigned below: task_name, title, description, start_date, end_date, is_completed and by split by a comma in 'taks.txt'
# the following will print out all task in the following order and format using (f.format) to place each variable in the rightfull order.
# the same applies for the following users
# task_file.close() and user_file.close() is used to close and save files

if username == "admin":
    choice = input("""
    Please select one of the following options:
    r - register user
    a - add task
    va - view all tasks
    vm - view my tasks
    s - display statistics of total number of task and users in txt
    e - exit
    """)

    if choice == "s":
        task_file = open("tasks.txt", "r")
        user_file = open("user.txt", "r")
        print("\nAll tasks below:")
        for line in task_file:
            task_name, title, description, start_date, end_date, is_completed = line.split(", ")

            print(f"""
            Username: {task_name}
            Title: {title}
            description = {description}
            Start date: {start_date}
            End date: {end_date}
            is_completed {is_completed}""")
        print("\nAll users below:")
        for line in user_file:
            user_name, password = line.split(", ")

            print(f"""
            Username: {user_name}
            Password: {password}
            """)
        task_file.close()
        user_file.close()

#********* choice "r" *********
    
# When user enter "r"
# if user choose "r" the following will take place
# user_file will be opened 'user.txt' and "a+" (append and write) to add and write to 'user.txt'
# username and password and confirm password will be asked to be entered (Rememeber it is only register)
# if password is equal to confirm then password and username will be written and added to "user_file" in user.txt

if choice == "r":
    #only admin is alllowed to register
    if username != "admin":
        print("error you not admin")
    if username == "admin":
        user_file = open("user.txt","a+")#I will need to append add this to user text
        
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        confirm = input("Please confirm password: ")

        for line in user_file:
            valid_password, valid_confirm = line.split(", ") #valid_confirm

        if password == confirm:
            user_file.write(f"\n{username}, {password}")
            print("Password match confirmed password")
            
        if login == False:
            print("Incorect details! confirmed password does not match password")
        user_file.close()

#********* choice "a" *********

## if user select "a". task_file will open "task.txt" and ask user a set of detials which will then be appended and writen in task_file
## the following will be asked of the user to be entered by the user below
##  The username of the person to whom the task is assigned.
##■ The title of the task.
##■ A description of the task.
##■ The date that the task was assigned to the user.
##■ The due date for the task.
##■ Either a ‘Yes’ or ‘No’ value that specifies if the task has been
##completed yet.

elif choice == "a":
    task_file = open("tasks.txt","a+")

    task_name = input("Enter the username of the assigned task: ")
    title = input("Enter the title of the task: ")
    description = input("Enter the desription of the task: ")
    start_date = input("Enter the start date the task was assigned to user: ")
    end_date = input("Enter the end date the task was assigned to user: ")
    is_completed = input("Is the task completed: ")

    task_file.write(f"\n{task_name}, {title}, {description}, {start_date}, {end_date}, {is_completed}")
    task_file.close()
    
#********* choice "va" *********

## if user select "va". task_file will open "tasks.txt" and all tasks will be read in set format
# for line in task_file the following will be assigned below: task_name, title, description, start_date, end_date, is_completed and by split by a comma in 'taks.txt'
# the following will print out all task in the following order and format using (f.format) to place each variable in the rightfull order.
# task_file.close() is used to close and save files
elif choice == "va":
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
    task_file.close()
    
#********* choice "vm" *********

## if user select "vm". task_file will open "tasks.txt" and a specific tasks will only be read in set format
# for line in task_file the following will be assigned below: task_name, title, description, start_date, end_date, is_completed and split by a comma in 'tasks.txt'
# if username (entered in login above) is equal to task_name in task_file (task.txt) then the below will only print out the task assigned by task_file
# the following will print out a specific task in the following order and format using (f.format) to place each variable in the rightfull order.
# task_file.close() is used to close and save files

elif choice == "vm":
    task_file = open("tasks.txt", "r")

    for line in task_file:
        task_name, title, description, start_date, end_date, is_completed = line.split(", ")

        if username == task_name:
            
            print(f"""
            Username: {username}
            Title: {title}
            description = {description}
            Start date: {start_date}
            End date: {end_date}
            is_completed {is_completed}""")
    task_file.close()
    
if choice == "e":
    print("Goodbye")
