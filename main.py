# Create a TO DO list application that runs in terminal. It should allow user to log in.
# Each user should have his own tasks in to do list. User should be able to add/ update/ delete tasks.
# User information and task information should be kept in database
# Database interactions should be handled by a separate object.
import helper
import db_crud

while True:
    choice = helper.choose_login_registration()
    if choice == 1:
        email = input('Email: ')
        password = input('Password: ')
        user = db_crud.select_user_by_password_email(email= email, password= password)
        if user == 'error':
            print('Wrong email or password')
            continue

        print(f'Login successfully: {user.username}')
        while True:
            choice = helper.user_choice()
            if choice == 1:
                task = input('Task: ')
                status = db_crud.add_task(task=task, user=user)
                if status == "error":
                    print(status)
                    continue
                print("Successfully save task")
            elif choice == 2:
                tasks = db_crud.user_tasks(user=user)
                for task in tasks:
                    print(f'{task.id}. {task.task}, {task.status}')
                choice = helper.user_choice_tasks()
                changing_task = db_crud.get_user_task_byid(task_id = choice)
                choice = helper.update_task_choice()
                if choice == 1:
                    name = input('Name: ')
                    status = db_crud.update_task(task=changing_task, name=name)
                    if status == "error":
                        print(status)
                        continue
                elif choice == 2:
                    statusas = input('Status: ')
                    status = db_crud.update_task(task=changing_task, status=statusas)
                    if status == "error":
                        print(status)
                        continue
            elif choice == 3:
                tasks = db_crud.user_tasks(user=user)
                for task in tasks:
                    print(f'{task.id}. {task.task}, {task.status}')
                choice = helper.user_choice_tasks()
                task = db_crud.get_user_task_byid(task_id=choice)
                status = db_crud.delete_task(task=task)
                if status == "error":
                    print(status)
                    continue
            elif choice == 4:
                tasks = db_crud.user_tasks(user=user)
                for task in tasks:
                    print(f'{task.task}, {task.status}')
    elif choice == 2:
        username = input('Username: ')
        password = input('Password: ')
        email = input('Email: ')
        status = db_crud.insert_user(username= username, password= password, email= email)
        if status == "success":
            print('Registration successful')
        else:
            print('Registration failed')
            continue

