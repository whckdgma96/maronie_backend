# from db_connect import db, Base
# from sqlalchemy.orm import relationship
# from sqlalchemy import Column, Integer, String, ForeignKey

# class Menu(db.Model):
#     __tablename__ = "menu"

#     id = db.Column(Integer, primary_key=True, nullable=False, autoincrement=True)
#     menu_name = db.Column(String(50), nullable=False)
#     image_path =db.Column(String(256), nullable=True)

# class Paring(db.Model):
#     __tablename__ = "paring"
    
#     id = db.Column(Integer, primary_key=True, nullable=False, autoincrement=True)
#     menu_id = db.Column(Integer, nullable=False)
#     classification_id = db.Column(Integer, nullable=False)