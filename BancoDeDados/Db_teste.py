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