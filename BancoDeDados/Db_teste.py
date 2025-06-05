from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

DataBase = create_engine("sqlite:///BancoDeDados/first_batabase.bd")
Session = sessionmaker(bind=DataBase)
session = Session()

base = declarative_base()

class User(base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True) #Inicia o Id e incrementa automáticamente
    name = Column("name", String)
    status = Column("status", Boolean)

    def __init__(self, name, status = True):
        self.name = name
        self.status = status

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nStatus: {self.status}"

class Book(base):
    __tablename__ = "books"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    status = Column("status", Boolean)
    owner = Column("owner", ForeignKey("users.id"))

    def __init__(self, name, owner, status = True):
        self.name = name
        self.owner = owner
        self.status = status
        
base.metadata.create_all(bind=DataBase)

# CRUD = Create/ Read/ Update/ Delete

user = User("Joseph3")
session.add(user)
session.commit()

users_list = session.query(User).all()
print(users_list)