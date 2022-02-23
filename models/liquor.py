from sqlalchemy.orm import relationship
from db_connect import db, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from .user import *

## N:M관계를 이렇게 만드는 것이 맞는지...
# By_liquor = db.Table('by_liquor',
#     Column('cocktail_id', db.Integer, db.ForeignKey('cocktail.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True),
#     Column('classification_id', db.Integer, db.ForeignKey('classification.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
# )

# Paring = db.Table('paring',
#     Column('menu_id', db.Integer, db.ForeignKey('menu.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True),
#     Column('classification_id', db.Integer, db.ForeignKey('classification.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
# )

class Liquor(db.Model):
    __tablename__ = "liquor"
   
    id = db.Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    liquor_name =db.Column(String(100), nullable=False)
    classification_id = db.Column(Integer, nullable=False)
    alcohol =db.Column(Float, nullable=True)
    price =db.Column(Integer, nullable=True)
    image_path = db.Column(String(256), nullable=True)
    description = db.Column(String(500), nullable=True) 
    vendor = db.Column(String(100), nullable=True)

    # ''' Liquor : classification은 1:N관계. relationship을 여기에 정의하는 것이 맞나? '''
    # # classification=relationship('Classification') 
    # classifications=relationship('Classification', backref=db.backref('liquor_set')) #backref 설정 해주어야 하나?
    # wish_liquor = relationship('Wishlist_liquor', secondary=Wishlist_liquor.__tablename__ , back_populates='liquor') #N:M
    # done_liquor = relationship('Done_liquor', secondary=Done_liquor.__tablename__ , back_populates='liquor') #N:M 
      

class Cocktail(db.Model):
    __tablename__ = "cocktail"
   
    id = db.Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    cocktail_name = db.Column(String(100), nullable=False)
    alcohol = db.Column(Float, nullable=True)
    ingredients = db.Column(String(100), nullable=False) 
    recipe = db.Column(String(500), nullable=False) 
    heart = db.Column(Integer, default=0, nullable=False)
    level = db.Column(Float, nullable=False)
    image_path = db.Column(String(100), nullable=True)
    description = db.Column(String(500), nullable=False) 

    # classifications = relationship('Classification', secondary=By_liquor.__tablename__ , back_populates='cocktail') #N:M
    # wish_cocktail = relationship('Wishlist_cocktail', secondary=Wishlist_cocktail.__tablename__ , back_populates='cocktail') #N:M
    # done_cocktail = relationship('Done_cocktail', secondary=Done_cocktail.__tablename__ , back_populates='cocktail') #N:M 

class Review(db.Model):
    __tablename__ = "review"
    id = db.Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(Integer, nullable=False )
    liquor_id = db.Column(Integer, nullable=False )
    content = db.Column(String(200), nullable=False)
    rating = db.Column(Float, nullable=False)
    review_date = db.Column(Date, nullable=True)

class Classification(db.Model):
    __tablename__ = "classification"

    id = db.Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    classification = db.Column(String(45), nullable=False)
    
    # menus = relationship('Menu', secondary=Paring.__tablename__ , back_populates='classification') #N:M
    # cocktails = relationship('Cocktail', secondary=By_liquor.__tablename__ , back_populates='classification') #N:M

class By_liquor(db.Model):
    __tablename__ = "by_liquor"

    id = db.Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    cocktail_id = db.Column(Integer, nullable=False)
    classification_id = db.Column(Integer, nullable=False)

