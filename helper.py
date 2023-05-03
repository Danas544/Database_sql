
def choose_login_registration():
    print("1. Login \n2. Register\n3. Exit")
    while True:
        try:
            choice = int(input())
        except ValueError:
            print("There are try choices 1, 2 or 3")
            continue
        if choice not in [1, 2, 3] or choice == str:
            print("There are try choices 1, 2 or 3")
            continue
        return choice

def user_choice():
    print("1. Add task \n2. Update task \n3. Delete task \n4. Tasks\n5. Exit")
    while True:
        try:
            choice = int(input())
        except ValueError:
            print("There are try choices 1, 2, 3, 4 or 5")
            continue
        if choice not in [1, 2, 3, 4, 5] or choice == str:
            print("There are try choices 1, 2, 3, 4 or 5")
            continue
        return choice

def user_choice_tasks():
    while True:
        try:
            choice = int(input("Choose task:"))
        except:
            continue
        return choice

def update_task_choice():
    while True:
        try:
            choice = int(input("1. Update task description \n2. Change status \n"))
        except:
            continue
        return choice
