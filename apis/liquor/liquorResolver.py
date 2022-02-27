from flask_restx import Resource, Namespace,fields
from flask import request

from . import liquorService

Liquor = Namespace(name="Liquor", description="Liquor")
liquor_fields = Liquor.model('Liquor', {
    'id': fields.Integer(description='Liquor id', required=True, example="1"),
    'liquor_name': fields.String(description='Liquor name', required=True, example="liquor_name"),
    'classification_id': fields.Integer(description='classification_id', required=True, example="1"),
    'alcohol': fields.Float(description='Liquor Alcohol', required=False, example="45"),
    'price': fields.Integer(description='Liquor Price', required=False, example="45000"),
    'image_path': fields.String(description='Image Path', required=False, example="image_path"),
    'description': fields.String(description='Description', required=True, example="abcdefg"),
    'vendor': fields.String(description='Vendor', required=False, example="경기도 용인시"),
    'rating': fields.Float(description='ration', required=False, example="4.5"),
})

Cocktail = Namespace(name="cocktail", description="Cocktail")
Cocktail_fields = Cocktail.model('Cocktail', {
    'id': fields.Integer(description='Cocktail id', required=True, example="1"),
    'cocktail_name': fields.String(description='Cocktail name', required=True, example="cocktail_name"),
    'alcohol': fields.Float(description='Cocktail Alcohol', required=False, example="45"),
    'ingredient': fields.String(description='Ingredient', required=True, example="ingredients"),
    'recipe': fields.String(description='Cocktail Recipe', required=True, example="recipes"),
    'heart': fields.Integer(description='heart', required=True, example="1"),
    'image_path': fields.String(description='Image Path', required=False, example="image_path"),
    'level': fields.Float(description='Difficulty level of cocktail', required=True, example="2"),
    'description': fields.String(description='Description', required=True, example="abcdefg"),
    
    
})
# 술 상세페이지 id로 조회
@Liquor.route('/detail_page/<int:liquor_id>')
class liquor_detailPage(Resource):
    @Liquor.response(200, "Liquor exist")
    @Liquor.response(404, "Not found")
    @Liquor.response(500, "Liquor doesn't exist")
    def get(self,liquor_id):
        '''술 id로 술 정보 조회'''
        return liquorService.liquor_detail_view(liquor_id)

# 칵테일 상세페이지
@Cocktail.route('/detail_page/<int:cocktail_id>')
class liquor_detailPage(Resource):
    @Liquor.response(200, "Available cocktail_id")
    @Liquor.response(404, "Not found")
    @Liquor.response(500, "Unavailable cocktail_id")
    def get(self,cocktail_id):
        '''칵테일 id로 정보 조회'''
        return liquorService.cocktail_detail_view(cocktail_id)

# 술 이름으로 검색
@Liquor.route('/search/<string:liquor_name>')
class liquor_detailPage(Resource):
    @Liquor.response(200, "Liquor exist")
    @Liquor.response(404, "Not found")
    @Liquor.response(500, "Liquor doesn't exist")
    def get(self,liquor_name):
        '''술 이름으로 정보 조회'''
        return liquorService.liquor_search_text(liquor_name)

# 칵테일 이름으로 검색
@Cocktail.route('/search/<string:cocktail_name>')
class liquor_detailPage(Resource):
    @Liquor.response(200, "Available cocktail_name")
    @Liquor.response(404, "Not found")
    @Liquor.response(500, "Unavailable cocktail_name")
    def get(self,cocktail_name):
        '''칵테일 이름으로 정보 조회'''
        return liquorService.cocktail_search_text(cocktail_name)




