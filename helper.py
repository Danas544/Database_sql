
def choose_login_registration():
    print("1. Login \n2. Register")
    while True:
        try:
            choice = int(input())
        except ValueError:
            print("There are try choices 1 or 2")
            continue
        if choice not in [1, 2] or choice == str:
            print("There are try choices 1 or 2")
            continue
        return choice

def user_choice():
    print("1. add task \n2. update task \n3. delete task \n4. tasks")
    while True:
        try:
            choice = int(input())
        except ValueError:
            print("There are try choices 1, 2, 3, 4")
            continue
        if choice not in [1, 2, 3, 4] or choice == str:
            print("There are try choices 1, 2, 3, 4")
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
            choice = int(input("1. Update task name \n2. Change status \n"))
        except:
            continue
        return choice
