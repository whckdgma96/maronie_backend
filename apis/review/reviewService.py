import os
from flask import abort, session
import pymysql
from models.liquor import *
from models.user import *
from db_connect import db
from datetime import datetime

def create_review(user_id:int,liquor_id:int,rating:float,content:str):
    # logined_user = User.query.filter_by(email=session['login']).first()
    # if logined_user.id != user_id:
    #     abort(500, "로그인 정보가 일치하지 않습니다.")
    review_date = datetime.today().strftime("%Y-%m-%d")
    review_check = Review.query.filter_by(user_id=user_id).filter_by(liquor_id=liquor_id).first()

    if review_check:
        abort(500, "이미 등록된 리뷰가 있습니다")
    else: 
        new_review = Review(user_id = user_id,liquor_id=liquor_id,rating=rating,content=content,review_date=review_date)
        db.session.add(new_review)
        db.session.commit()
        db.session.close()
        return {"message":"리뷰등록 성공"},201

        

def update_review(user_id:int,review_id:int,rating:float,content:str):
    try:
        # logined_user = User.query.filter_by(email=session['login']).first()
        # if logined_user.id != user_id:
        #     abort(500, "로그인 정보가 일치하지 않습니다.")
        """UPDATE review SET rating=%s, content=%s, review_date=%s WHERE user_id=%s AND id=%s"""
        review_check = Review.query.filter_by(user_id=user_id, id=review_id).first()
        if not review_check:
            abort(500, "등록된 리뷰가 없습니다.")
        
        else:
            review_check.rating = rating
            review_check.content = content
            review_check.review_date = datetime.today().strftime("%Y-%m-%d")
            db.session.commit()
            return {"message":"리뷰수정 성공"},200
    finally:
        db.session.close()

def delete_review(user_id:int, review_id:int):
    """DELETE from review WHERE user_id=%s AND id=%s"""
    # logined_user = User.query.filter_by(email=session['login']).first()
    # if logined_user.id != user_id:
    #     abort(500, "로그인 정보가 일치하지 않습니다.")
    review_check = Review.query.filter_by(user_id=user_id, id=review_id).first()
    if not review_check:
        abort(500, "등록된 리뷰가 없습니다.")
    else:
        db.session.delete(review_check)
        db.session.commit()
        db.session.close()
        return {"message":"리뷰삭제 성공"},200

def get_review(user_id:int, review_id:int):
    #로그인 여부 판별 생략
    review = Review.query.filter_by(id=review_id).first()
    return review

def get_next_reviews(liquor_id:int, last_review_id:int):
    reviews = Review.query.filter(Review.id > last_review_id).filter_by(liquor_id = liquor_id).limit(10).all()
    try:
        result = {'last_review_id' : reviews[-1].id, 'liquor_id' : reviews[-1].liquor_id, 'reviews': reviews}
        return result
    except Exception as ex:
        print(ex)
        return 
