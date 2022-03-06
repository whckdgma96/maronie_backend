from flask import abort, session
from flask_restx import marshal
from models.liquor import Liquor, Cocktail, Review
from models.paring import Paring
from db_connect import db

# 술 상세페이지 id로 조회
def liquor_detail_view(liquor_id:int):
    liquor = Liquor.query.filter_by(id = liquor_id).first()
    cocktail = Cocktail.query.filter_by(classification_id = liquor.classification_id).all()
    paring = Paring.query.filter_by(classification_id =liquor.classification_id).limit(3).all()
    reviews = Review.query.filter_by(liquor_id = liquor_id).all()
    '''
    별점분포 ? 이런식으로 db.session으로 연결해서 쿼리문 날리기 시도해보자...
    timerank = db.session.query(FoodHour.food, func.sum(FoodHour.count).label('total')).filter(
                FoodHour.hour == curr_hour).group_by(FoodHour.food).order_by(desc('total')).limit(3).all()

            sbq = db.session.query(FoodHour.food, (func.sum(
                FoodHour.count)/24).label('avg')).group_by(FoodHour.food).subquery()

            timeraterank = db.session.query(FoodHour.food, (func.sum(FoodHour.count)/sbq.c.avg).label('rate')).join(sbq, sbq.c.food == FoodHour.food).filter(
                FoodHour.hour == curr_hour).group_by(FoodHour.food).order_by(desc('rate')).limit(3).all()

    '''
    result = {'liquor' : liquor, 'paring' : paring, 'cocktail' : cocktail, 'review' :reviews}
    if liquor:
        return result,200 #성공
    else: 
        abort(500, "Unavailable liquor_id")

# 칵테일 상세페이지 id로 조회
def cocktail_detail_view(cocktail_id:int):
    cocktail = Cocktail.query.filter_by(id=cocktail_id).first()

    if cocktail:
        return cocktail,200  
    else: 
        abort(500, "Unavailable cocktail_id")

#칵테일 레시피 등록
def create_cocktail_recipe(data):
    try:
        author_id = data['author_id']
        cocktail_name=data["cocktail_name"]
        cocktail_name_kor= data["cocktail_name_kor"]
        classification_id= data["classification_id"]
        level = data["level"]
        alcohol = data["alcohol"]
        description = data["description"]
        image_path = data["image_path"]
        ingredients = '\n'.join(data["ingredients"])
        recipe = '\n'.join(data["recipe"])
        
        new_cocktail = Cocktail(author_id=author_id, cocktail_name=cocktail_name, cocktail_name_kor=cocktail_name_kor,
                                classification_id=classification_id, level=level, alcohol=alcohol,
                                description=description, image_path=image_path, ingredients=ingredients, recipe=recipe)  
        db.session.add(new_cocktail)
        db.session.commit()
        return {"message":"recipe successfully created"},201 #성공
    except Exception as ex:
        print(ex)
        return {"message":"Fail to create"},500 #실패
        
