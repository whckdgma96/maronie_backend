from flask import abort, session
from flask_restx import marshal
from models.liquor import *
from models.paring import *
from models.user import *
from db_connect import db

def wishlist(user_id:int):
    # logined_user = User.query.filter_by(email=session['login']).first()

    # if logined_user.id != user_id:
    #     abort(500, "로그인 정보가 일치하지 않습니다.")
    # else:
    wishlist_liquor = Wishlist_liquor.query.filter_by(user_id = user_id).all()
    wishlist_cocktail = Wishlist_cocktail.query.filter_by(user_id = user_id).all()
    liquors=[]
    cocktails=[]
    print(wishlist_liquor)
    for i in range(len(wishlist_liquor)):
        liquor = Liquor.query.filter_by(id = wishlist_liquor[i].liquor_id).all()
        liquors += liquor
    for i in range(len(wishlist_cocktail)):
        cocktail = Cocktail.query.filter_by(id = wishlist_cocktail[i].cocktail_id).all()
        cocktails += cocktail
    
    result = {"liquor": liquors, "cocktail":cocktails}

    return result,200