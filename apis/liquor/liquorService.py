from db_connect import db

from models.liquor import Liquor
from models.liquor import Cocktail

# from models.liquor import Cocktail
# def liquor_detail_view(liquor_name:str):
#     liquor = Liquor.query.filter_by(liquor_name=liquor_name).first()
#     if liquor:
#         return {
#             "id":liquor.id,
#             "classification_id":liquor.classification_id,
#             "rating" : liquor.rating,
#             "description" : liquor.description
#         },200 #성공
#     else: 
#         return {"message":"Not found"},404

def liquor_detail_view(liquor_id:int):
    liquor = Liquor.query.filter_by(id = liquor_id).first()
    if liquor:
        return {
            "liquor_name":liquor.liquor_name,
            # "classification_id":liquor.classification_id,
            "rating" : liquor.rating,
            # "description" : liquor.description
        },200 #성공
    else: 
        return {"message":"Not found"},404

def liquor_search_text(liquor_name:str):
    liquor = Liquor.query.filter(Liquor.liquor_name.like('%'+liquor_name+'%')).first()
    if liquor:
        return {
            "liquor_name":liquor.liquor_name,
            # "classification_id":liquor.classification_id,
            "rating" : liquor.rating,
            # "description" : liquor.description
        },200 #성공
    else: 
        return {"message":"Not found"},404

def cocktail_detail_view(cocktail_id:int):
    cocktail = Cocktail.query.filter_by(id=cocktail_id).first()
    if cocktail:
        return {
            "id":cocktail.id,
            "name" : cocktail.cocktail_name,
            "ingredient":cocktail.ingredients,
            "recipe" : cocktail.recipe,
            "level":cocktail.level,
            "description" : cocktail.description
        },200 #성공
    else: 
        return {"message":"Not found"},404

def cocktail_search_text(cocktail_name:str):
    cocktail = Cocktail.query.filter(Cocktail.cocktail_name.like('%'+cocktail_name+'%')).first()
    if cocktail:
        return {
            "id":cocktail.id,
            "name" : cocktail.cocktail_name,
            "ingredient":cocktail.ingredients,
            "recipe" : cocktail.recipe,
            "level":cocktail.level,
            "description" : cocktail.description
        },200 #성공
    else: 
        return {"message":"Not found"},404