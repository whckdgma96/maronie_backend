import os
from flask import abort
from sqlalchemy import null
from apis.liquor.save_file_utils import save_image
from models.liquor import Liquor, Cocktail, Review
from models.paring import Paring
from db_connect import db
from models.user import User

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
def create_cocktail_recipe(thumbnail, data):
    try:
        author_id = data['author_id']
        cocktail_name = null()
        if "cocktail_name" in data:
            cocktail_name=data["cocktail_name"]
        cocktail_name_kor= data["cocktail_name_kor"]
        classification_id= data["classification_id"]
        level = data["level"]
        alcohol = null()
        if "alcohol" in data:
            alcohol = data["alcohol"]
        description = data["description"]
        ingredients = data["ingredients"]
        recipe = data['recipe']
        image_path= null()
        image_path= save_image(thumbnail, False) #is_search=False
        new_cocktail = Cocktail(author_id=author_id, cocktail_name=cocktail_name, cocktail_name_kor=cocktail_name_kor,
                                classification_id=classification_id, level=level, alcohol=alcohol,
                                description=description, image_path=image_path, ingredients=ingredients, recipe=recipe)  
        db.session.add(new_cocktail)
        db.session.commit()

        return {"message":"recipe successfully created"},201 #성공

    except Exception as ex:
        print(ex)
        return ex, 500 #실패
        
def update_cocktail_recipe(user_id:int, cocktail_id:int, thumbnail, data):
    '''로그인 여부 판별(생략)'''
    # logined_user = User.query.filter_by(email=session['login']).first()
    # if logined_user.id != user_id:
    #     abort(500, "로그인 정보가 일치하지 않습니다.")
    try:
        '''기존 이미지 삭제'''
        cocktail = Cocktail.query.filter_by(id = cocktail_id).first()
        old_path=str(cocktail.image_path)
        #조건문은 모든 테이블의 image_path 속성을 모두 not null로 바꾼후 삭제 (혹은 try로 바꾸기. remove는 없는 파일을 삭제하면 에러가 난다)
        if os.path.isfile(str(old_path)):
            os.remove(old_path)
        
        '''새로운 이미지 저장 후 주소 추가'''
        updated_data = data.to_dict()
        new_path = save_image(thumbnail)
        updated_data['image_path'] = new_path

        '''db 업데이트'''
        db.session.query(Cocktail).filter(Cocktail.id==cocktail_id).update(updated_data)
        db.session.commit()

        '''
        #이렇게 하면 안됨. 에러는 안나지만 데이터베이스가 업데이트가 안됨.
        cocktail = db.session.query(Cocktail).filter(Cocktail.id==cocktail_id).first()
        for key in data.to_dict().keys():
            print(data[key])
            cocktail.key = data[key]
        db.session.save()
        db.session.commit()
        '''
        
        return {"message":"cocktail recipe successfully updated"}, 200
    except Exception as ex:
        return ex, 500

def delete_cocktail_recipe(user_id:int, cocktail_id:int):
    '''로그인 여부 판별(생략)'''
    # logined_user = User.query.filter_by(email=session['login']).first()
    # if logined_user.id != user_id:
    #     abort(500, "로그인 정보가 일치하지 않습니다.")
    try:
        cocktail = db.session.query(Cocktail).filter(Cocktail.id==cocktail_id).first()
        db.session.delete(cocktail)
        db.session.commit()
        
        return {"message":"cocktail recipe successfully deleted"}, 200

    except Exception as ex:
        return ex, 500
