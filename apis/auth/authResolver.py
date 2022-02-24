from flask_restx import Resource
from flask import request
from .authDTO import *
from . import authService

# Auth = Namespace(name="auth", description="사용자 인증")
# user_fields = Auth.model('User', {
#     'id': fields.String(description='User Id', required=True, example="1234"),
#     'email': fields.String(description='User Email', required=True, example="CCH@naver.com"),
#     'password': fields.String(description='User Password', required=True, example="password"),
#     'nickname': fields.String(description='User Nickname', required=True, example="CCH")
# })

# #DTO

# # checkIdDTO = Auth.model('checkId',{
# #     'email': fields.String(description='User Email', required=True, example="CCH@naver.com")
# # }) #얜 안댐

# registerDTO = Auth.model('User_register', {
#     'email': fields.String(description='User Email', required=True, example="CCH@naver.com"),
#     'password': fields.String(description='User Password', required=True, example="password"),
#     'nickname': fields.String(description='User Nickname', required=True, example="CCH")
# })

# loginDTO = Auth.model('User_login', {
#     'email': fields.String(description='User Email', required=True, example="CCH@naver.com"),
#     'password': fields.String(description='User Password', required=True, example="password")
# })
# changepwDTO = Auth.model('pw_change', {
#     'email': fields.String(description='User Email', required=True, example="CCH@naver.com"),
#     'password': fields.String(description='New User Password', required=True, example="password"),
#     'nickname': fields.String(description='User Nickname', required=True, example="CCH")
# })

# 회원가입 유효성
@Auth.route('/register/<string:email>')
class AuthRegisterCheckId(Resource):
    # @Auth.expect(checkIdDTO)
    @Auth.response(200, "Available email address")
    @Auth.response(404, "Not found")
    @Auth.response(500, "Unavailable email address")
    def get(self,email):
        '''회원가입시 ID유효성 검사'''
        return authService.idckeck(email)

# 회원가입 요청
@Auth.route('/register')
class AuthRegister(Resource):
    @Auth.expect(registerDTO)
    # @Auth.response(200, "Available id")
    # @Auth.response(500, "Unavailable id")
    def post(self):
        '''회원가입 성공시 DB에 저장'''
        email = request.json['email']
        nickname = request.json['nickname']
        password = request.json['password']
        return authService.userRegister(email,nickname,password)

# 로그인
@Auth.route('/login')
class AuthLogin(Resource):
    @Auth.expect(loginDTO)
    @Auth.response(200, "login Success")
    @Auth.response(404, "Not found")
    @Auth.response(500, "login Failed")
    def post(self):
        '''로그인 기능'''
        email = request.json['email']
        password = request.json['password']
        return authService.userLogin(email,password)

#비밀번호 변경

@Auth.route('/changepw')
class AuthChangepw(Resource):
    @Auth.expect(changepwDTO)
    @Auth.response(200, "password Changed")
    @Auth.response(404, "Not Found")
    @Auth.response(404, "Wrong Password")
    @Auth.response(500, "Password Change Fail")
    def post(self):
        '''유저 비밀번호 변경하기'''
        email = request.json['email']
        new_password = request.json['new_password']
        new_password_check = request.json['new_password_check']
        return authService.changepw(email,new_password,new_password_check)

# 로그아웃
@Auth.route('/logout')
class AuthLogout(Resource):
    def post(self):
        '''로그아웃 기능'''
        return authService.userLogout()
