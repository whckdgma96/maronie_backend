from flask_restx import Resource
from flask import request, session, abort
from .mypageDTO import *
from . import mypageService
# wishlist 출력
@Mypage.route('/wishlist/<int:user_id>')
class wishlist(Resource):
    @Mypage.response(200,"success",wishlist_response)
    @Mypage.response(500, "fail")
    @Mypage.marshal_with(wishlist_response, mask=False)
    def get(self, user_id):
        '''wishlist 출력'''
        # if not session:
        #     abort(500, "로그인 해주세요")
        # else:
        return mypageService.wishlist(user_id)

# liquor wishlist 추가
@Mypage.route('/wishlist/create/liquor')
class create_wishlist_liquor(Resource):
    @Mypage.expect(create_wishlist_liquor)
    @Mypage.response(200,"success")
    @Mypage.response(500, "fail")
    def post(self):
        '''liquor wishlist 추가'''
        user_id = request.json['user_id']
        liquor_id = request.json['liquor_id']

        return mypageService.create_wishlist_liquor(user_id,liquor_id)

# cocktail wishlist 추가
@Mypage.route('/wishlist/create/cocktail')
class create_wishlist_cocktail(Resource):
    @Mypage.expect(create_wishlist_cocktail)
    @Mypage.response(200,"success")
    @Mypage.response(500, "fail")
    def post(self):
        '''cocktail wishlist 추가'''
        user_id = request.json['user_id']
        cocktail_id = request.json['cocktail_id']

        return mypageService.create_wishlist_cocktail(user_id,cocktail_id)

# liquor wishlist 삭제
@Mypage.route('/wishlist/delete/<int:user_id>/liquor/<int:liquor_id>')
class delete_wishlist_liquor(Resource):
    @Mypage.response(200,"success")
    @Mypage.response(500, "fail")
    def delete(self, user_id, liquor_id):
        '''liquor wishlist 삭제'''
        return mypageService.delete_wishlist_liquor(user_id,liquor_id)

# cocktail wishlist 삭제
@Mypage.route('/wishlist/delete/<int:user_id>/cocktail/<int:cocktail_id>')
class delete_wishlist_cocktail(Resource):
    @Mypage.response(200,"success")
    @Mypage.response(500, "fail")
    def delete(self, user_id, cocktail_id):
        '''cocktail wishlist 삭제'''
        return mypageService.delete_wishlist_cocktail(user_id,cocktail_id)


# donelist 출력
@Mypage.route('/donelist/<int:user_id>')
class donelist(Resource):
    @Mypage.response(200,"success",donelist_response)
    @Mypage.response(500, "fail")
    @Mypage.marshal_with(donelist_response, mask=False)
    def get(self, user_id):
        '''donelist 출력'''
        # if not session:
        #     abort(500, "로그인 해주세요")
        # else:
        return mypageService.donelist(user_id)

# liquor donelist 추가
@Mypage.route('/donelist/create/liquor')
class create_donelist_liquor(Resource):
    @Mypage.expect(create_donelist_liquor)
    @Mypage.response(200,"success")
    @Mypage.response(500, "fail")
    def post(self):
        '''liquor donelist 추가'''
        user_id = request.json['user_id']
        liquor_id = request.json['liquor_id']

        return mypageService.create_donelist_liquor(user_id,liquor_id)

# cocktail donelist 추가
@Mypage.route('/donelist/create/cocktail')
class create_donelist_cocktail(Resource):
    @Mypage.expect(create_donelist_cocktail)
    @Mypage.response(200,"success")
    @Mypage.response(500, "fail")
    def post(self):
        '''cocktail donelist 추가'''
        user_id = request.json['user_id']
        cocktail_id = request.json['cocktail_id']

        return mypageService.create_donelist_cocktail(user_id,cocktail_id)

# liquor donelist 삭제
@Mypage.route('/donelist/delete/<int:user_id>/liquor/<int:liquor_id>')
class delete_donelist_liquor(Resource):
    @Mypage.response(200,"success")
    @Mypage.response(500, "fail")
    def delete(self, user_id, liquor_id):
        '''liquor donelist 삭제'''
        return mypageService.delete_donelist_liquor(user_id,liquor_id)

# cocktail donelist 삭제
@Mypage.route('/donelist/delete/<int:user_id>/cocktail/<int:cocktail_id>')
class delete_donelist_cocktail(Resource):
    @Mypage.response(200,"success")
    @Mypage.response(500, "fail")
    def delete(self, user_id, cocktail_id):
        '''cocktail donelist 삭제'''
        return mypageService.delete_donelist_cocktail(user_id,cocktail_id)

# 칵테일 레시피 모아보기
@Mypage.route('/recipe/<int:user_id>')
class my_cocktail_recipe(Resource):
    @Mypage.response(200,"success",my_cocktail_recipe)
    @Mypage.response(500, "fail")
    @Mypage.marshal_with(my_cocktail_recipe, mask=False)
    def get(self, user_id):
        '''칵테일 레시피 모아보기'''
        return mypageService.my_cocktail_recipe(user_id)


# 내가쓴 리뷰 모아보기
@Mypage.route('/review/<int:user_id>')
class my_review(Resource):
    @Mypage.response(200,"success",my_review)
    @Mypage.response(500, "fail")
    @Mypage.marshal_with(my_review, mask=False)
    def get(self, user_id):
        '''내가쓴 리뷰 모아보기'''
        return mypageService.my_review(user_id)