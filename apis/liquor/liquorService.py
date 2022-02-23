from db_connect import db

from models.liquor import Liquor

def detail_view(liquor_id:int):
    liquor = Liquor.query.filter_by(id=liquor_id).first()
    if liquor:
        return {
            "liquor_name":liquor.liquor_name,
            "classification_id":liquor.classification_id,
            "rating" : liquor.rating,
            "description" : liquor.description
        },200 #성공
    else: 
        return {"message":"Not found"},404
    