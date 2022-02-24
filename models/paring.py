from db_connect import db
from sqlalchemy.orm import relationship

'''
sqlalchemy xxver. 이상 추천 : back_populates (출처 찾지 못함)
nullable : Defaults to True unless Column.primary_key is also True 
           or the column specifies a Identity, in which case it defaults to False
'''


class Menu(db.Model):
    __tablename__ = "menu"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    menu_name = db.Column(db.String(50), nullable=False)
    image_path = db.Column(db.String(256))
    parings = relationship("Menu", back_populates="menus")

class Paring(db.Model):
    __tablename__ = "paring"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    classification_id = db.Column(db.Integer, db.ForeignKey('classification.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    menus = relationship("Paring", back_populates="parings")