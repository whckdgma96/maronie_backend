import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")

# print(SECRET_KEY)
BASE_DIR = os.path.dirname(__file__) # 폴더 구조가 달라져도, 현재 폴더를 가져와서 사용할 수 있도록 설정합니다.

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://team11:AIteam11Liquor@127.0.0.1:3306/Liquor" 

SQLALCHEMY_TRACK_MODIFICATIONS = False