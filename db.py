from sqlalchemy import create_engine
from sqlalchemy.orm.decl_api import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from models import Users, Tasks
from typing import Optional , Union
class SqliteDatabase:
    def __init__(self, db_name:str, base: DeclarativeMeta):
        self.db_name = db_name
        self.Base = base
        self.engine = create_engine(f"sqlite:///{self.db_name}")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create_detabase(self):
        self.Base.metadata.create_all(self.engine, checkfirst=True)

    def insert_user(self,username: str, password: str, email: str) -> bool:
        user = Users(username=username, password=password, email=email)
        self.session.add(user)
        try:
            self.session.commit()
            return True
        except:
            return False

    def select_user_by_password_email(self, email: str, password: str) -> Union[Users,bool]:
        user = self.session.query(Users).filter(Users.email == email, Users.password == password).first()
        if user is None:
            return False
        return user

    def add_task(self, user, task) -> bool:
        task = Tasks(description=task, user=user)
        self.session.add(task)
        try:
            self.session.commit()
            return True
        except:
            return False

    def user_tasks(self, user):
        task = self.session.query(Tasks).filter(Tasks.user_id == user.id)
        if task.count() == 0:
            return False
        return task

    def get_user_task_byid(self, task_id, user):
        task = self.session.query(Tasks).filter(Tasks.id == task_id, Tasks.user_id == user.id).first()
        return task

    def update_task(self, task, name=None, status=None) -> bool:
        if task is None:
            return False
        if name is not None:
            task.description = name
            try:
                self.session.commit()
                return True
            except:
                return False
        task.status = status
        try:
            self.session.commit()
            return True
        except:
            return False

    def delete_task(self, task) -> bool:
        if task is None:
            return False
        self.session.delete(task)
        try:
            self.session.commit()
            return True
        except:
            return False

if __name__ == '__main__':
    pass