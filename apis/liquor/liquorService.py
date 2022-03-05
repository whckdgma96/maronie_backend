import json
from flask import abort

from models.liquor import Liquor, Cocktail, Review
from models.paring import Paring

# 술 상세페이지 id로 조회
def liquor_detail_view(liquor_id:int):
    liquor = Liquor.query.filter_by(id = liquor_id).first()
    cocktail = Cocktail.query.filter_by(classification_id = liquor.classification_id).all()
    paring = Paring.query.filter_by(classification_id =liquor.classification_id).limit(3).all()
    reviews = Review.query.filter_by(liquor_id = liquor_id).all()
  
    result = {'liquor' : liquor, 'paring' : paring, 'cocktail' : cocktail, 'review' :reviews}
    if liquor:
        return result,200 #성공
    else: 
        abort(500, "Unavailable liquor_id")


# 칵테일 상세페이지 id로 조회
def cocktail_detail_view(cocktail_id:int):
    cocktail = Cocktail.query.filter_by(id=cocktail_id).first()

    if cocktail:
        return cocktail,200  
    else: 
        abort(500, "Unavailable cocktail_id")

