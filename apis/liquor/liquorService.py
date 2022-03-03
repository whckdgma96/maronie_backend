from db_connect import db

from models.liquor import Liquor, By_liquor, Cocktail, Review
from models.paring import Menu, Paring
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

'''
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
# 술 상세페이지 id로 조회
def liquor_detail_view(liquor_id:int):
    liquor = Liquor.query.filter_by(id = liquor_id).first()
    by_liquor = By_liquor.query.filter_by(classification_id = liquor.classification_id).all()
    paring = Paring.query.filter_by(classification_id =liquor.classification_id).limit(3).all()
    # review = Review.query.filter_by(liquor_id = liquor_id).all()
    result = {'liquor' : liquor, 'paring' : paring, 'cocktail' : by_liquor }
    if liquor:
        return result,200 #성공
    else: 
        return {"message":"Not found"},404



# 칵테일 상세페이지 id로 조회

def cocktail_detail_view(cocktail_id:int):
    cocktail = Cocktail.query.filter_by(id=cocktail_id).first()
    ingred = cocktail.ingredients
    recipe = cocktail.recipe

    ingred = ingred.split('\\n')
    recipe = recipe.split('\\n')
    result = {'result1':cocktail,'result2':{"ingredients":ingred,"recipe" :recipe}}
    if cocktail:
        # return {
        #     "cocktail_name" : cocktail.cocktail_name,
        #     "alcohol": cocktail.alcohol,
        #     "ingredient":ingred.split('\\n'),
        #     "recipe" : recipe.split('\\n'),
        #     "level":cocktail.level,
        #     "description" : cocktail.description
        # },200 #성공
        return result,200
        # {
        #     "ingredients":ingred.split('\\n'),
        #     "recipe" : recipe.split('\\n')
        #     }
    else: 
        return {"message":"Not found"},404


# 술 이름으로 조회
# def liquor_search_text(liquor_name:str):
#     liquor = Liquor.query.filter(Liquor.liquor_name.like('%'+liquor_name+'%')).first()
#     if liquor:
#         return {
#             "liquor_name":liquor.liquor_name,
#             # "classification_id":liquor.classification_id,
#             "rating" : liquor.rating,
#             # "description" : liquor.description
#         },200 #성공
#     else: 
#         return {"message":"Not found"},404

# # 칵테일 이름으로 조회

# def cocktail_search_text(cocktail_name:str):
#     cocktail = Cocktail.query.filter(Cocktail.cocktail_name.like('%'+cocktail_name+'%')).first()
#     if cocktail:
#         return {
#             "id":cocktail.id,
#             "name" : cocktail.cocktail_name,
#             "ingredient":cocktail.ingredients,
#             "recipe" : cocktail.recipe,
#             "level":cocktail.level,
#             "description" : cocktail.description
#         },200 #성공
#     else: 
#         return {"message":"Not found"},404