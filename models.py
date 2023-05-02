import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import engine


Base = sqlalchemy.orm.declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column('username',String)
    password = Column('password',String)
    email = Column('email',String, unique=True)




class Tasks(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    task = Column('task',String)
    status = Column('status',String , default='Created')
    user_id = Column('user_id',Integer, ForeignKey('users.id'))
    user = relationship("Users")


if __name__ == "__main__":
    Base.metadata.create_all(engine)


