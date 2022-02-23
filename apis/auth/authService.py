from flask import request,session
from models.user import User
from models.liquor import *
from db_connect import db
import bcrypt #pip install bcrypt (암호화, 암호일치 확인)

# 회원가입 유효성

def idckeck(email:str):
    new_user = User.query.filter_by(email=email).first() # id 가 동일한 유저의 정보 저장
    if new_user: return {"message":"Unavailable email"},500 #결과값이 있다면 = 등록된 유저
    else: return {"message":"Available email"},200

# 회원가입 요청

def userRegister(email:str,nickname:str, password:str):
    
    encrypted_pw = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
    new_user = User(email=email, nickname=nickname, password=encrypted_pw) #area도 추후 추가
    db.session.add(new_user)
    db.session.commit()
    return {"message":"User Information saved"},200 #성공

# 로그인

def userLogin(email: str, password:str):
    saved_user = User.query.filter_by(email=email).first()
    
    #유효하지 않은 ID
    if not saved_user: return{
            "message": "User Not Found"
        }, 404
    # 비밀번호 미일치
    elif not bcrypt.checkpw(password.encode("utf-8"),saved_user.password.encode("utf-8") ):
        return {
            "message": "Auth Failed"
        }, 500
    # 모두 일치
    else: 
        session['login'] = saved_user.email
        return {
            # "message": "login Success ",
            "name":saved_user.nickname,
            "email":saved_user.email
        },200

#비밀번호 변경

def changepw(email,nickname,new_password):
    conn = pymysql.connect(host='127.0.0.1',port=3306, user='root', password='root', db='liquor', charset='utf8')
    cur = conn.cursor()
    #DB연결 후 메서드 호출
    saved_user = User.query.filter_by(email=email).first()
    sql = """UPDATE user SET password =%s WHERE nickname =%s"""
    encrypted_pw = bcrypt.hashpw(new_password.encode('utf8'),bcrypt.gensalt())
    if not saved_user: 
        return{
            "message":"User Not Found"
        },404
    elif nickname != saved_user.nickname:
        return{
            "message":"User nickname isn't correct"
        },500
    else: 
        cur.execute(sql, (encrypted_pw, saved_user.nickname))
        conn.commit()
        return {
            "message":"password changed"
        },200

# 로그아웃

def userLogout():
    session.clear()
    return {"message":"logout success"},200


