import os

BASE_DIR = os.path.dirname(__file__) # 폴더 구조가 달라져도, 현재 폴더를 가져와서 사용할 수 있도록 설정합니다.

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:team11@127.0.0.1:3306/Liquor"

                            #통신방식          #패스워드는 team11
# SQLALCHEMY_BINDS = "mysql+pymysql://root:team11@127.0.0.1:3306/Liquor"#두개이상 db이용할때 사용

SQLALCHEMY_TRACK_MODIFICATIONS = False
