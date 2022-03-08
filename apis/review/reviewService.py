from flask import abort, session
import pymysql
from models.liquor import *
from models.user import *
from db_connect import db
from datetime import datetime

def create_review(user_id:int,liquor_id:int,rating:float,content:str):
    
    logined_user = User.query.filter_by(email=session['login']).first()

    review_date = datetime.today().strftime("%Y-%m-%d")
    # print(review_date)
    review_check = Review.query.filter_by(user_id=user_id).filter_by(liquor_id=liquor_id).first()
    if not session:
        abort(500, "로그인 해주세요")
    
    elif logined_user.id != user_id:
        abort(500, "로그인 정보가 일치하지 않습니다.")
    elif review_check: # 있는 리뷰 -> 업데이트를 해야댐
        abort(500, "이미 등록된 리뷰가 있습니다")
    else: 
        new_review = Review(user_id = user_id,liquor_id=liquor_id,rating=rating,content=content,review_date=review_date)
        db.session.add(new_review)
        db.session.commit()
        return {"message":"리뷰등록 성공"},201

def update_review(user_id:int,liquor_id:int,rating:float,content:str):
    logined_user = User.query.filter_by(email=session['login']).first()
    conn = pymysql.connect(host='127.0.0.1',port=3306, user='team11', password='AIteam11Liquor', db='liquor', charset='utf8') #숨기기
    cur = conn.cursor()
    sql = """UPDATE review SET rating=%s, content=%s, review_date=%s WHERE user_id=%s AND liquor_id=%s"""
    review_date = datetime.today().strftime("%Y-%m-%d")
    review_check = Review.query.filter_by(user_id=user_id).filter_by(liquor_id=liquor_id).first()
    if not session:
        abort(500, "로그인 해주세요")
    
    elif logined_user.id != user_id:
        abort(500, "로그인 정보가 일치하지 않습니다.")
    elif not review_check:
        abort(500, "등록된 리뷰가 없습니다.")
    
    else:
        cur.execute(sql,(rating,content,review_date,user_id,liquor_id))
        conn.commit()
        return {"message":"리뷰수정 성공"},200
    