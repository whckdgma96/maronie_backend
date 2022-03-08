from flask_restx import Resource
from flask import request, session, abort
from .mypageDTO import *
from . import mypageService

@Mypage.route('/wishlist=<int:user_id>')
class wishlist(Resource):
    @Mypage.response(200,"success",wishlist_response)
    @Mypage.response(500, "fail")
    @Mypage.marshal_with(wishlist_response, mask=False)

    def get(self, user_id):
        # if not session:
        #     abort(500, "로그인 해주세요")
        # else:
        return mypageService.wishlist(user_id)
