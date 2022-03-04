from distutils.log import error
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
        return 500