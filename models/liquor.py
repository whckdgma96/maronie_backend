from sqlalchemy.orm import relationship
from db_connect import db, Base
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

class Paring(Base):
    __tablename__ = "paring"

    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    classification_id = db.Column(db.Integer, db.ForeignKey('classification.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)

class By_liquor(Base):
    __tablename__ = "by_liquor"

    cocktail_id = db.Column(db.Integer, db.ForeignKey('cocktail.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    classification_id = db.Column(db.Integer, db.ForeignKey('classification.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)

class Wishlist_liquor(Base):
    __tablename__ = "wishlist_liquor"

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    liquor_id = db.Column(db.Integer, db.ForeignKey('liquor.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)

class Wishlist_cocktail(Base):
    __tablename__ = "wishlist_cocktail"

    cocktail_id = db.Column(db.Integer, db.ForeignKey('cocktail.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)

class Done_liquor(Base):
    __tablename__ = "done_liquor"

    liquor_id = db.Column(db.Integer, db.ForeignKey('liquor.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)

class Done_cocktail(Base):
    __tablename__ = "done_cocktail"

    cocktail_id = db.Column(db.Integer, db.ForeignKey('cocktail.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)

    
class Liquor(Base):
    __tablename__ = "liquor"
   
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    liquor_name =db.Column(db.String(100))
    classification_id = db.Column(db.Integer, db.ForeignKey('classification.id', ondelete='CASCADE', onupdate='CASCADE'))
    alcohol =db.Column(db.Float, nullable=True)
    price =db.Column(db.Integer, nullable=True)
    image_path =db.Column(db.String(100), nullable=True)
    description =db.Column(db.String(500)) 
    vendor =db.Column(db.String(100), nullable=True)

    ''' Liquor : classification은 1:N관계. relationship을 여기에 정의하는 것이 맞나? '''
    # classification=relationship('Classification') 
    classifications=relationship('Classification', backref=db.backref('liquor_set')) #backref 설정 해주어야 하나?
    wish_liquor = relationship('Wishlist_liquor', secondary=Wishlist_liquor.__tablename__ , back_populates='liquor') #N:M
    done_liquor = relationship('Done_liquor', secondary=Done_liquor.__tablename__ , back_populates='liquor') #N:M 
      

class Cocktail(Base):
    __tablename__ = "cocktail"
   
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cocktail_name =db.Column(db.String(100))
    alcohol =db.Column(db.Float, nullable=True)
    ingredients =db.Column(db.String(100)) 
    recipe =db.Column(db.String(500)) 
    heart =db.Column(db.Integer, default=0)
    level = db.Column(db.Float)
    image_path =db.Column(db.String(100), nullable=True)
    description =db.Column(db.String(500)) 

    classifications = relationship('Classification', secondary=By_liquor.__tablename__ , back_populates='cocktail') #N:M
    wish_cocktail = relationship('Wishlist_cocktail', secondary=Wishlist_cocktail.__tablename__ , back_populates='cocktail') #N:M
    done_cocktail = relationship('Done_cocktail', secondary=Done_cocktail.__tablename__ , back_populates='cocktail') #N:M 


class Classification(Base):
    __tablename__ = "classification"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    classification = db.Column(db.String(45))
    
    menus = relationship('Menu', secondary=Paring.__tablename__ , back_populates='classification') #N:M
    cocktails = relationship('Cocktail', secondary=By_liquor.__tablename__ , back_populates='classification') #N:M

class Menu(Base):
    __tablename__ = "menu"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    menu_name = db.Column(db.String(50))
    image_path =db.Column(db.String(100), nullable=True)
    
    classifications = relationship('Classification', secondary=Paring.__tablename__, back_populates='menu') #N:M

class Review(Base):
    __tablename__ = "review"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'))
    liquor_id = db.Column(db.Integer, db.ForeignKey('liquor.id', ondelete='CASCADE', onupdate='CASCADE'))
    content = db.Column(db.String(200))
    rating = db.Column(db.Float)
    review_date = db.Column(db.Date, nullable=True)



