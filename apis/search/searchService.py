from distutils.log import error
import os
import shutil
from flask import abort, flash
from apis.liquor.save_file_utils import save_image
from config import UPLOAD_FOLDER #app.config['UPLOAD_FOLDER']를 import하는것에 실패
from .predict import predict_liquor
from models.liquor import Liquor
from models.liquor import Cocktail
from .searchDTO import *
    
def search_keyword(keyword:str):
    #검색할 때 if문을 두어서 키워드가 영어인지 한국어인지 판단하고 검색하는것이 좋을까?
    #아니면 그냥 항상 두 컬럼을 조회하는 것이 빠를까?
    liquor = Liquor.query.filter(Liquor.liquor_name_kor.like('%'+keyword+'%') | 
                                 Liquor.liquor_name.like('%'+keyword+'%')).all()
    cocktail = Cocktail.query.filter(Cocktail.cocktail_name_kor.like('%'+keyword+'%') | 
                                     Cocktail.cocktail_name.like('%'+keyword+'%')).all()

    '''정의한 DTO와 형식을 맞추어준다'''
    result = {"liquor":liquor, "cocktail":cocktail}
    try:
        return result, 200
    except:
        #에러 종류 프린트
        #better : flask logger
        print(error)


def search_image(liquor_image):
    if 'file' not in liquor_image:
        flash('No file part')
        return abort(500,'No file part')

    test_img = liquor_image['file']

    image_path = save_image(test_img)

    predicted_id = predict_liquor(image_path)

    if predicted_id == -1:
        return abort(500,'해당되는 이미지를 찾을 수 없습니다')

    predicted_liquor = Liquor.query.filter_by(id = predicted_id).first()
    new_path = os.path.join(UPLOAD_FOLDER, predicted_liquor.liquor_name)

    os.makedirs(new_path, exist_ok=True)
    shutil.move(image_path, new_path)
    
    return  predicted_liquor
    