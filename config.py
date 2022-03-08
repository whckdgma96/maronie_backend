import os
import dotenv 

dotenv.load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
# print(SECRET_KEY)

BASE_DIR = os.path.dirname(__file__) # 폴더 구조가 달라져도, 현재 폴더를 가져와서 사용할 수 있도록 설정합니다.

SQLALCHEMY_DATABASE_URI = (f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@"
                           f"127.0.0.1:{os.getenv('MYSQL_PORT')}"
                           f"/{os.getenv('MYSQL_DATABASE')}"
                          )

SQLALCHEMY_TRACK_MODIFICATIONS = False

UPLOAD_FOLDER = "./media/upload"
COCKTAIL_THUMBNAIL_FOLDER = "./media/cocktail_thumbnail"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}