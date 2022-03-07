from flask import request
from flask_restx import Resource
from . import searchService
from .searchDTO import *


# 술 이름으로 검색
@Search.route('=<string:keyword>')
class search_keyword(Resource):
    @Search.response(200, "success", result_text_response)
    @Search.response(500, "fail")
    @Search.marshal_with(result_text_response, mask=False)
    def get(self,keyword):
        '''술/칵테일 이름으로 정보 조회'''
        return searchService.search_keyword(keyword)

#술 이미지로 검색
@Search.route('/file-upload')
class search_image(Resource):
    @Search.expect(image_liquor)
    @Search.response(200, "success", result_image_response)
    @Search.response(500, "fail")
    @Search.marshal_with(result_image_response, mask=False)
    def post(self):
        liquor_image = request.files
        return searchService.search_image(liquor_image=liquor_image)


