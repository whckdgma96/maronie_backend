from flask_restx import Resource, Namespace,fields
from flask import request

from . import liquorService

Liquor = Namespace(name="Liquor", description="술 상세페이지")
liquor_fields = Liquor.model('Liquor', {
    'id': fields.Integer(description='Liquor id', required=True, example="1"),
    # 'liquor_name': fields.String(description='Use', required=False, example="CCH@naver.com"),
    # 'password': fields.String(description='User Password', required=True, example="password"),
    # 'nickname': fields.Integer(description='User Nickname', required=True, example="CCH")
})

# 술 상세페이지
@Liquor.route('/detail_page/<int:liquor_id>')
class liquor_detailPage(Resource):
    @Liquor.response(200, "Available liquor_id")
    @Liquor.response(404, "Not found")
    @Liquor.response(500, "Unavailable liquor_id")
    def get(self,liquor_id):
        '''술 id로 술 정보 조회'''
        return liquorService.detail_view(liquor_id)