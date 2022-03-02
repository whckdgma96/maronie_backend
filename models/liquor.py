from sqlalchemy.orm import relationship
from db_connect import db


class Classification(db.Model):
    __tablename__ = "classification"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    classification = db.Column(db.String(45), nullable=False)
    
    c_liquors = relationship("Liquor", back_populates="classifications")
    c_cocktails = relationship("By_liquor", back_populates="classifications")


class Liquor(db.Model):
    __tablename__ = "liquor"
   
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    liquor_name = db.Column(db.String(100), nullable=False)
    liquor_name_kor = db.Column(db.String(45), nullable=False)
    classification_id = db.Column(db.Integer, db.ForeignKey('classification.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    alcohol = db.Column(db.Float)
    price = db.Column(db.Integer)
    image_path = db.Column(db.String(256))
    description = db.Column(db.Text, nullable=False) 
    vendor = db.Column(db.String(256))
    rating = db.Column(db.Float, nullable=False, default=0)

    classifications = relationship("Classification", back_populates="c_liquors")
    liquor_reviews = relationship("Review", back_populates="reviewed_liquors")
    wish_l = relationship("Wishlist_liquor", back_populates="wish_l_info")
    done_l = relationship("Donelist_liquor", back_populates="done_l_info")


class Cocktail(db.Model):
    __tablename__ = "cocktail"
   
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cocktail_name = db.Column(db.String(100), nullable=False)
    cocktail_name_kor = db.Column(db.String(45), nullable=False)
    alcohol = db.Column(db.Float)
    ingredients = db.Column(db.String(100), nullable=False) 
    recipe = db.Column(db.String(500), nullable=False) 
    heart = db.Column(db.Integer, default=0, nullable=False)
    level = db.Column(db.Float, nullable=False)
    image_path = db.Column(db.String(256))
    description = db.Column(db.Text, nullable=False) 

    wish_c = relationship("Wishlist_cocktail", back_populates="wish_c_info")
    done_c = relationship("Donelist_cocktail", back_populates="done_c_info")
    base = relationship("By_liquor", back_populates="cocktails")


class Review(db.Model):
    __tablename__ = "review"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False )
    liquor_id = db.Column(db.Integer, db.ForeignKey('liquor.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False )
    content = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review_date = db.Column(db.Date)

    reviewed_users = relationship("User", back_populates="user_reviews")
    reviewed_liquors = relationship("Liquor", back_populates="liquor_reviews")


class By_liquor(db.Model):
    __tablename__ = "by_liquor"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cocktail_id = db.Column(db.Integer, db.ForeignKey('cocktail.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    classification_id = db.Column(db.Integer, db.ForeignKey('classification.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    classifications = relationship("Classification", back_populates="c_cocktails")
    cocktails = relationship("Cocktail", back_populates="base")