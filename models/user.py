from db_connect import db
from sqlalchemy.orm import relationship


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    nickname = db.Column(db.String(45), nullable=False)

    wish_liquors = relationship("Wishlist_liquor", back_populates="wish_l_users")
    wish_cocktails = relationship("Wishlist_cocktail", back_populates="wish_c_users")
    done_liquors = relationship("Donelist_liquor", back_populates="done_l_users")
    done_cocktails = relationship("Donelist_cocktail", back_populates="done_c_users")
    user_reviews = relationship("Review", back_populates="reviewed_users")

'''북마크 기능. 먹어보고 싶거나 관심있는 술을 담아둔다.'''
class Wishlist_liquor(db.Model):
    __tablename__ = "wishlist_liquor"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    liquor_id = db.Column(db.Integer, db.ForeignKey('liquor.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    wish_l_users = relationship("User", back_populates="wish_liquors")
    wish_l_info = relationship("Liquor", back_populates="wish_l")


class Wishlist_cocktail(db.Model):
    __tablename__ = "wishlist_cocktail"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    cocktail_id = db.Column(db.Integer, db.ForeignKey('cocktail.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    wish_c_users = relationship("User", back_populates="wish_cocktails")
    wish_c_info = relationship("Cocktail", back_populates="wish_c")


'''먹어봤어요 기능'''
class Donelist_liquor(db.Model):
    __tablename__ = "donelist_liquor"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    liquor_id = db.Column(db.Integer, db.ForeignKey('liquor.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    done_l_users = relationship("User", back_populates="done_liquors")
    done_l_info = relationship("Liquor", back_populates="done_l")


class Donelist_cocktail(db.Model):
    __tablename__ = "donelist_cocktail"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    cocktail_id = db.Column(db.Integer, db.ForeignKey('cocktail.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    done_c_users = relationship("User", back_populates="done_cocktails")
    done_c_info = relationship("Cocktail", back_populates="done_c")


# def init_db(): #to-do) 따로 파일로 빼기
#     db.create_all()
    
# if __name__ == '__main__':
#     init_db()