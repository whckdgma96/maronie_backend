import os
from flask import abort, flash, session
from flask_restx import marshal
from sqlalchemy import null
from apis.search.searchService import allowed_file, naming_file
from config import ALLOWED_EXTENSIONS, COCKTAIL_THUMBNAIL_FOLDER
from models.liquor import Liquor, Cocktail, Review
from models.paring import Paring
from werkzeug.utils import secure_filename
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
def create_cocktail_recipe(cocktail_thumbnail, data):
    try:
        author_id = data['author_id']
        cocktail_name = None #(NULL) 이 아니라 비어있게 진짜 null로 만들고 싶은데,,,
        if "cocktail_name" in data:
            cocktail_name=data["cocktail_name"]
        cocktail_name_kor= data["cocktail_name_kor"]
        classification_id= data["classification_id"]
        level = data["level"]
        alcohol = None
        if "alcohol" in data:
            alcohol = data["alcohol"]
        description = data["description"]
        ingredients = data["ingredients"]
        recipe = data['recipe']

        cocktail_img = cocktail_thumbnail['file']

        if cocktail_img.filename == '':
            flash('No selected file')
            return abort(500,'No selected file')
        if cocktail_img and allowed_file(cocktail_img.filename):
            filename = naming_file(secure_filename(cocktail_img.filename))
            image_path = os.path.join(COCKTAIL_THUMBNAIL_FOLDER, filename)
            cocktail_img.save(image_path)

        new_cocktail = Cocktail(author_id=author_id, cocktail_name=cocktail_name, cocktail_name_kor=cocktail_name_kor,
                                classification_id=classification_id, level=level, alcohol=alcohol,
                                description=description, image_path=image_path, ingredients=ingredients, recipe=recipe)  
        db.session.add(new_cocktail)
        db.session.commit()
        return {"message":"recipe successfully created"},201 #성공
    except Exception as ex:
        print(ex)
        return {"message":"Fail to create"},500 #실패
        
