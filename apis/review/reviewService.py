from flask import abort, session
import pymysql
from models.liquor import *
from models.user import *
from db_connect import db
from datetime import datetime


def create_review(user_id:int,liquor_id:int,rating:float,content:str):
    review_date = datetime.today().strftime("%Y-%m-%d")
    # print(review_date)
    review_check = Review.query.filter_by(user_id=user_id).filter_by(liquor_id=liquor_id).first()
    if review_check: # 있는 리뷰 -> 업데이트를 해야댐
        abort(500, "이미 리뷰를 등록했습니다")
    else: 
        new_review = Review(user_id = user_id,liquor_id=liquor_id,rating=rating,content=content,review_date=review_date)
        db.session.add(new_review)
        db.session.commit()
        return {"message":"리뷰등록 성공"},200