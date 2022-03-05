from flask_restx import Resource
from .liquorDTO import *
from . import liquorService

# 술 상세페이지 id로 조회
@Liquor.route('=<int:liquor_id>')
class liquor_detailPage(Resource):
    @Liquor.response(200, "Liquor exist", liquor_detail_response)
    @Liquor.response(404, "Not found")
    @Liquor.response(500, "Liquor doesn't exist")
    @Liquor.marshal_with(liquor_detail_response, mask=False)
    def get(self,liquor_id):
        '''술 id로 술 정보 조회'''
        return liquorService.liquor_detail_view(liquor_id)

# 칵테일 상세페이지 id로 조회
@Cocktail.route('=<int:cocktail_id>')
class liquor_detailPage(Resource):
    @Cocktail.response(200, "Available cocktail_id",cocktail_detail_response)
    @Cocktail.response(404, "Not found")
    @Cocktail.response(500, "Unavailable cocktail_id")
    # @Cocktail.marshal_with(cocktail_detail_response , mask=False)
    def get(self,cocktail_id):
        '''칵테일 id로 정보 조회'''
        return liquorService.cocktail_detail_view(cocktail_id)







