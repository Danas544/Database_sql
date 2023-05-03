import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship



Base = sqlalchemy.orm.declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column('username',String)
    password = Column('password',String)
    email = Column('email',String, unique=True)
    tasks = relationship("Tasks", back_populates="user")






class Tasks(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    description = Column('description',String)
    status = Column('status',String , default='Created')
    user_id = Column('user_id',Integer, ForeignKey('users.id'))
    user = relationship("Users", back_populates="tasks")
    def __repr__(self) -> str:
        return f"{self.description}, {self.status}, {self.user_id}"


if __name__ == "__main__":
    pass


