import json
from flask import abort
from flask_restx import marshal
from .liquorDTO import cocktail_detail_response
from models.liquor import Liquor, By_liquor, Cocktail, Review
from models.paring import Paring

# 술 상세페이지 id로 조회
def liquor_detail_view(liquor_id:int):
    liquor = Liquor.query.filter_by(id = liquor_id).first()
    by_liquor = By_liquor.query.filter_by(classification_id = liquor.classification_id).all()
    paring = Paring.query.filter_by(classification_id =liquor.classification_id).limit(3).all()

    result = {'liquor' : liquor, 'paring' : paring, 'cocktail' : by_liquor }
    if liquor:
        return result,200 #성공
    else: 
        abort(500, "Unavailable liquor_id")


# 칵테일 상세페이지 id로 조회
def cocktail_detail_view(cocktail_id:int):
    cocktail = Cocktail.query.filter_by(id=cocktail_id).first()

    if cocktail:
        result = marshal(cocktail,cocktail_detail_response)
        result['ingredients'] = cocktail.ingredients.split('\\n')
        result['recipe'] = cocktail.recipe.split('\\n')
        return result,200  
    else: 
        abort(500, "Unavailable cocktail_id")


'''
#without 'marshal_with'
def liquor_detail_view(liquor_id:int):
    liquor = Liquor.query.filter_by(id = liquor_id).first()
    by_liquor = By_liquor.query.filter_by(classification_id = liquor.classification_id).first()
    cocktail = Cocktail.query.filter_by(id =by_liquor.cocktail_id).first()

    paring = Paring.query.filter_by(classification_id =liquor.classification_id).first()
    menu = Menu.query.filter_by(id =paring.menu_id).first()
    if liquor:
        return {
            "liquor_name":liquor.liquor_name,
            "alcohol": liquor.alcohol,
            "classification_id":liquor.classification_id,
            "price":liquor.price,
            "image_path":liquor.image_path,
            "rating" : liquor.rating,
            "description" : liquor.description,
            "paring":[{"menu":menu.menu_name,"menu_image":menu.image_path}],
            "cocktail":[{'cocktail_name':cocktail.cocktail_name, "cocktail_image":cocktail.image_path}],
        },200 #성공
    else: 
        return {"message":"Not found"},404
'''