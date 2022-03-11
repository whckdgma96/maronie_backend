import os
from flask import abort, session
import pymysql
from models.liquor import *
from models.user import *
from db_connect import db
from datetime import datetime

def create_review(user_id:int,liquor_id:int,rating:float,content:str):
    
    # logined_user = User.query.filter_by(email=session['login']).first()
    logined_user = User.query.filter_by(email=session).first()

    review_date = datetime.today().strftime("%Y-%m-%d")
    # print(review_date)
    review_check = Review.query.filter_by(user_id=user_id).filter_by(liquor_id=liquor_id).first()

    
    if logined_user.id != user_id:
        abort(500, "로그인 정보가 일치하지 않습니다.")
    elif review_check: # 있는 리뷰 -> 업데이트를 해야댐
        abort(500, "이미 등록된 리뷰가 있습니다")
    else: 
        new_review = Review(user_id = user_id,liquor_id=liquor_id,rating=rating,content=content,review_date=review_date)
        db.session.add(new_review)
        db.session.commit()
        return {"message":"리뷰등록 성공"},201

def update_review(user_id:int,review_id:int,rating:float,content:str):
    # logined_user = User.query.filter_by(email=session['login']).first()
    conn = pymysql.connect(host=os.getenv('MYSQL_HOST'),
                           port=int(os.getenv('MYSQL_PORT')), 
                           user=os.getenv('MYSQL_USER'), 
                           password=os.getenv('MYSQL_PASSWORD'), 
                           db=os.getenv('MYSQL_DATABASE'), 
                           charset='utf8') #숨기기
    cur = conn.cursor()
    sql = """UPDATE review SET rating=%s, content=%s, review_date=%s WHERE user_id=%s AND id=%s"""
    review_date = datetime.today().strftime("%Y-%m-%d")
    review_check = Review.query.filter_by(user_id=user_id).filter_by(id=review_id).first()
    
    # if logined_user.id != user_id:
    #     abort(500, "로그인 정보가 일치하지 않습니다.")
    if not review_check:
        abort(500, "등록된 리뷰가 없습니다.")
    
    else:
        cur.execute(sql,(rating,content,review_date,user_id,review_id))
        conn.commit()
        return {"message":"리뷰수정 성공"},200

def delete_review(user_id:int, review_id:int):
    # logined_user = User.query.filter_by(email=session['login']).first()
    conn = pymysql.connect(host=os.getenv('MYSQL_HOST'), 
                          port=int(os.getenv('MYSQL_PORT')),
                          user=os.getenv('MYSQL_USER'), 
                          password=os.getenv('MYSQL_PASSWORD'), 
                          db=os.getenv('MYSQL_DATABASE'), charset='utf8')
 
    cur = conn.cursor()
    sql= """DELETE from review WHERE user_id=%s AND id=%s"""
    review_check = Review.query.filter_by(user_id=user_id).filter_by(id=review_id).first()
    # if logined_user.id != user_id:
    #     abort(500, "로그인 정보가 일치하지 않습니다.")
    if not review_check:
        abort(500, "등록된 리뷰가 없습니다.")
    else:
        cur.execute(sql,(user_id, review_id))
        conn.commit()
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
