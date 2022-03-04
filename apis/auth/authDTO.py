from flask_restx import Namespace,fields

Auth = Namespace(name="auth", description="사용자 인증")

# checkIdDTO = Auth.model('checkId', {
#     'email': fields.String(description='User Email', required=True, example="CCH@gmail.com")
# }) 

registerDTO = Auth.model('User_register', {
    'email': fields.String(description='User Email', required=True, example="CCH@gmail.com"),
    'password': fields.String(description='User Password', required=True, example="password1"),
    'nickname': fields.String(description='User Nickname', required=True, example="CCH")
})

loginDTO = Auth.model('User_login', {
    'email': fields.String(description='User Email', required=True, example="CCH@gmail.com"),
    'password': fields.String(description='User Password', required=True, example="password1")
})

changepwDTO = Auth.model('pw_change', {
    'email': fields.String(description='User Email', required=True, example="CCH@gmail.com"),
    'new_password': fields.String(description='New User Password', required=True, example="password2"),
    # 'new_password_check': fields.String(description='New User Password check', required=True, example="password2"),
})

login_response = Auth.model('login_response',{
    'id' : fields.Integer(description='User Id',required=True, example="2" ),
    'email': fields.String(description='User Email', required=True, example="CCH@gmail.com"),
    'nickname' : fields.String(description='User nickname', required=True,example="CCH")
})

