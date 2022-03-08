from flask_restx import Resource
from flask import request, session, abort
from .mypageDTO import *
from . import mypageService
# 위시리스트 출력
@Mypage.route('/wishlist=<int:user_id>')
class wishlist(Resource):
    @Mypage.response(200,"success",wishlist_response)
    @Mypage.response(500, "fail")
    @Mypage.marshal_with(wishlist_response, mask=False)

    def get(self, user_id):
        '''위시리스트 출력'''
        # if not session:
        #     abort(500, "로그인 해주세요")
        # else:
        return mypageService.create_wishlist(user_id)

# liquor 위시리스트 추가
@Mypage.route('/wishlist/liquor')
class create_wishlist_liquor(Resource):
    @Mypage.expect(create_wishlist_liquor)
    @Mypage.response(200,"success")
    @Mypage.response(500, "fail")

    def post(self):
        '''# liquor 위시리스트 추가'''
        user_id = request.json['user_id']
        liquor_id = request.json['liquor_id']

        return mypageService.create_wishlist_liquor(user_id,liquor_id)

# cocktail 위시리스트 추가
@Mypage.route('/wishlist/cocktail')
class create_wishlist_cocktail(Resource):
    @Mypage.expect(create_wishlist_cocktail)
    @Mypage.response(200,"success")
    @Mypage.response(500, "fail")

    def post(self):
        '''cocktail 위시리스트 추가'''
        user_id = request.json['user_id']
        cocktail_id = request.json['cocktail_id']

        return mypageService.create_wishlist_cocktail(user_id,cocktail_id)

# liquor 위시리스트 삭제
@Mypage.route('/wishlist/delete/user_id=<int:user_id>/liquor_id=<int:liquor_id>')
class delete_wishlist_liquor(Resource):
    @Mypage.response(200,"success")
    @Mypage.response(500, "fail")

    def delete(self, user_id, liquor_id):
        '''liquor 위시리스트 삭제'''
        return mypageService.delete_wishlist_liquor(user_id,liquor_id)

# cocktail 위시리스트 삭제
@Mypage.route('/wishlist/delete/user_id=<int:user_id>/cocktail_id=<int:cocktail_id>')
class delete_wishlist_cocktail(Resource):
    @Mypage.response(200,"success")
    @Mypage.response(500, "fail")

    def delete(self, user_id, cocktail_id):
        '''cocktail 위시리스트 삭제'''
        return mypageService.delete_wishlist_cocktail(user_id,cocktail_id)