from db import session
from models import Users, Tasks


def insert_user(username: str, password: str, email: str) -> str:
    user = Users(username=username, password=password, email=email)
    session.add(user)
    try:
        session.commit()
        return 'success'
    except:
        return 'error'


def select_user_by_password_email(email: str, password: str):
    user = session.query(Users).filter(Users.email == email, Users.password == password).first()
    if user is None:
        return 'error'
    return user

def add_task(user, task):
    task = Tasks(task=task, user=user)
    session.add(task)
    try:
        session.commit()
        return 'success'
    except:
        return 'error'


def user_tasks(user):
    task = session.query(Tasks).filter(Tasks.user_id == user.id)
    return task

def get_user_task_byid(task_id):
    task = session.query(Tasks).get(task_id)
    return task

def update_task(task, name = None , status = None):
    if name is not None:
        task.task = name
        try:
            session.commit()
            return 'success'
        except:
            return 'error'
    task.status = status
    try:
        session.commit()
        return 'success'
    except:
        return 'error'

def delete_task(task):
    session.delete(task)
    try:
        session.commit()
        return 'success'
    except:
        return 'error'