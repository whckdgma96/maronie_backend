from db_connect import db, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    menu_name = Column(String(50), nullable=False)
    image_path =Column(String(256), nullable=True)

class Paring(Base):
    __tablename__ = "paring"
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    menu_id = Column(Integer, nullable=False)
    classification_id = Column(Integer, nullable=False)