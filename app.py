# -*- coding: utf-8 -*-
from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api
from flask_cors import CORS

from db_connect import db
import config
    
def create_app():
    app = Flask(__name__)
    CORS(app)
    
    from apis.auth.authResolver import Auth
    from apis.liquor.liquorResolver import Liquor
    from apis.liquor.liquorResolver import Cocktail
    from apis.search.searchResolver import Search
    from apis.review.reviewResolver import Review
    # from apis.paring.paringResolver import paring

    app.config.from_object(config)  # config 에서 가져온 파일을 사용합니다.

    db.init_app(app)  # SQLAlchemy 객체를 app 객체와 이어줍니다.
    Migrate().init_app(app, db)
    
    app.secret_key = config.SECRET_KEY #.env 사용
    app.config['SESSION_TYPE'] = 'filesystem' #Redis대신 filesystem사용

    #blueprint로 한번에 묶기
    api = Api(app)
    api.add_namespace(Auth, '/auth')
    api.add_namespace(Liquor, '/liquor')
    api.add_namespace(Cocktail, '/cocktail')
    api.add_namespace(Search, '/search')
    api.add_namespace(Review, '/review')
    return app

if __name__ == "__main__":
    create_app().run(host='0.0.0.0', debug=True, )
