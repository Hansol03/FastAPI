from sqlalchemy import Boolean, Column, Integer, String
from database import Base
# Base: parameter. database.py 파일에서 만든 Base class import 및 상속

class Todos(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
