from db_connect import db, Base
from sqlalchemy.orm import relationship
# from .liquor import Wishlist_cocktail, Wishlist_liquor, Done_liquor, Done_cocktail

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    email = db.Column(db.String(100),nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    nickname = db.Column(db.String(45), nullable=False)

# class User(Base):
#     __tablename__ = "user"
#     id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
#     email = db.Column(db.String(100),nullable=False, unique=True)
#     password = db.Column(db.String(255), nullable=False)
#     nickname = db.Column(db.String(45), nullable=False)

#     wish_liquor = relationship('Wishlist_liquor', secondary=Wishlist_liquor.__tablename__ , back_populates='user') #N:M
#     wish_cocktail = relationship('Wishlist_cocktail', secondary=Wishlist_cocktail.__tablename__ , back_populates='user') #N:M
#     done__liquor = relationship('Done_liquor', secondary=Done_liquor.__tablename__ , back_populates='user') #N:M
#     done_cocktail = relationship('Done_cocktail', secondary=Done_cocktail.__tablename__ , back_populates='user') #N:M

def init_db(): #to-do) 따로 파일로 빼기
    db.create_all()
    
if __name__ == '__main__':
    init_db()