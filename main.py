# Create a TO DO list application that runs in terminal. It should allow user to log in.
# Each user should have his own tasks in to do list. User should be able to add/ update/ delete tasks.
# User information and task information should be kept in database
# Database interactions should be handled by a separate object.
import helper
from db import SqliteDatabase
from models import Base
from sqlalchemy.orm.decl_api import DeclarativeMeta


class App:
    def __init__(self, DB):
        self.DB = DB

    def run(self):
        while True:
            choice = helper.choose_login_registration()
            if choice == 1:
                email = input('Email: ')
                password = input('Password: ')
                user = self.DB.select_user_by_password_email(email=email, password=password)
                if user is False:
                    print('Wrong email or password')
                    continue

                print(f'Login successfully: {user.username}')
                while True:
                    choice = helper.user_choice()
                    if choice == 1:
                        task = input('Description: ')
                        status = self.DB.add_task(task=task, user=user)
                        if status is False:
                            print('Error')
                            continue
                        print("Successfully save task")
                    elif choice == 2:
                        tasks = self.DB.user_tasks(user=user)
                        print('________________________________________________________________')
                        if tasks is False:
                            print('Not found tasks')
                            print('________________________________________________________________')
                            continue
                        for task in tasks:
                            print(f'{task.id}. {task.description}, {task.status}')
                        print('________________________________________________________________')
                        choice = helper.user_choice_tasks()
                        changing_task = self.DB.get_user_task_byid(task_id=choice , user=user)
                        choice = helper.update_task_choice()
                        if choice == 1:
                            name = input('Description: ')
                            status = self.DB.update_task(task=changing_task, name=name)
                            if status is False:
                                print('Error')
                                continue
                        elif choice == 2:
                            statusas = input('Status: ')
                            status = self.DB.update_task(task=changing_task, status=statusas)
                            if status is False:
                                print('Error')
                                continue
                    elif choice == 3:
                        tasks = self.DB.user_tasks(user=user)
                        print('________________________________________________________________')
                        if tasks is False:
                            print('Not found tasks')
                            print('________________________________________________________________')
                            continue
                        for task in tasks:
                            print(f'{task.id}. {task.description}, {task.status}')
                        print('________________________________________________________________')
                        choice = helper.user_choice_tasks()
                        task = self.DB.get_user_task_byid(task_id=choice , user=user)
                        status = self.DB.delete_task(task=task)
                        if status is False:
                            print('Error')
                            continue
                    elif choice == 4:
                        tasks = self.DB.user_tasks(user=user)
                        print('________________________________________________________________')
                        if tasks is False:
                            print('Not found tasks')
                            print('________________________________________________________________')
                            continue
                        for task in tasks:
                            print(f'{task.description}, {task.status}')
                        print('________________________________________________________________')
                    elif choice == 5:
                        exit()
            elif choice == 2:
                username = input('Username: ')
                password = input('Password: ')
                email = input('Email: ')
                status = self.DB.insert_user(username=username, password=password, email=email)
                if status is True:
                    print('Registration successful')
                else:
                    print(f'Registration failed this email {email} is in use')
                    continue
            elif choice == 3:
                exit()

DB = SqliteDatabase(db_name='todolist.db', base=Base)
DB.create_detabase()
start = App(DB)


if __name__ == '__main__':
    start.run()

