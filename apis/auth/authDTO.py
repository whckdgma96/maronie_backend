from flask_restx import Namespace,fields

Auth = Namespace(name="auth", description="사용자 인증")
# user_fields = Auth.model('User', {
#     'id': fields.String(description='User Id', required=True, example="1234"),
#     'email': fields.String(description='User Email', required=True, example="CCH@naver.com"),
#     'password': fields.String(description='User Password', required=True, example="password"),
#     'nickname': fields.String(description='User Nickname', required=True, example="CCH")
# })

checkIdDTO = Auth.model('checkId', {
    'email': fields.String(description='User Email', required=True, example="CCH@naver.com")
}) #얜 안댐

registerDTO = Auth.model('User_register', {
    'email': fields.String(description='User Email', required=True, example="CCH@naver.com"),
    'password': fields.String(description='User Password', required=True, example="password"),
    'nickname': fields.String(description='User Nickname', required=True, example="CCH")
})

loginDTO = Auth.model('User_login', {
    'email': fields.String(description='User Email', required=True, example="CCH@naver.com"),
    'password': fields.String(description='User Password', required=True, example="password")
})
changepwDTO = Auth.model('pw_change', {
    'email': fields.String(description='User Email', required=True, example="CCH@naver.com"),
    'new_password': fields.String(description='New User Password', required=True, example="password2"),
    'new_password_check': fields.String(description='New User Password check', required=True, example="password2"),
})

