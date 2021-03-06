from flask import abort, session
import pymysql
from models.user import User
from models.liquor import *
from db_connect import db
import bcrypt #pip install bcrypt (암호화, 암호일치 확인)
from .authDTO import *
import os

# 회원가입 email 유효성 검사
# TO-DO: try except로 바꾸기(처리속도 향상)
def idckeck(email:str):
    new_user = User.query.filter_by(email=email).first() # id 가 동일한 유저의 정보 저장
    if new_user: return {"message":"Unavailable email"},500 #결과값이 있다면 = 등록된 유저
    else: return {"message":"Available email"},200

# 회원가입 nickname 유효성 검사
def nicknameckeck(nickname:str):
    new_user = User.query.filter_by(nickname=nickname).first() # id 가 동일한 유저의 정보 저장
    if new_user: return {"message":"Unavailable nickname"},500 #결과값이 있다면 = 등록된 유저
    else: return {"message":"Available nickname"},200

# 회원가입 요청
def userRegister(email:str, nickname:str, password:str):
    encrypted_pw = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
    try:
        new_user = User(email=email, nickname=nickname, password=encrypted_pw) #area도 추후 추가
        db.session.add(new_user)
        db.session.commit()
        db.session.close()
        return {"message":"User Information saved"},201 #성공
    except:
        return {"message":"Register Failed"},500 #실패

# 로그인
def userLogin(email: str, password:str):
    saved_user = User.query.filter_by(email=email).first()
    
    #유효하지 않은 ID
    if not saved_user: 
        abort(500, "User Not Found")
    # 비밀번호 미일치
    elif not bcrypt.checkpw(password.encode("utf-8"),saved_user.password.encode("utf-8") ):
        abort(500, "Auth Failed(Wrong password)")
    # 모두 일치
    else: 
        session['login'] = saved_user.email
        print(session['login'])

        return saved_user,200

#비밀번호 변경
def changepw(email,new_password):
    conn = pymysql.connect(host=os.getenv('MYSQL_HOST'),port=int(os.getenv('MYSQL_PORT')), user=os.getenv('MYSQL_USER'), password=os.getenv('MYSQL_PASSWORD'), db=os.getenv('MYSQL_DATABASE'), charset='utf8') #숨기기
    cur = conn.cursor()
    #DB연결 후 메서드 호출
    saved_user = User.query.filter_by(email=email).first()
    sql = """UPDATE user SET password =%s WHERE nickname =%s"""
    
    if not saved_user: 
        return{
            "message":"User Not Found"
        },404
    
    else: 
        encrypted_pw = bcrypt.hashpw(new_password.encode('utf8'),bcrypt.gensalt())
        cur.execute(sql, (encrypted_pw, saved_user.nickname))
        conn.commit()
        conn.close()
        return {
            "message":"password changed"
        },201

# 로그아웃
def userLogout():
    if not session:
        return {"message":"로그인 정보가 없습니다."},500
    else:
        session.pop('login',None)
        return {"message":"logout success"},200


