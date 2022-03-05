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






