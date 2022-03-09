from flask_restx import Resource
from flask import request
# from flask_login import login_required
from .liquorDTO import *
from . import liquorService

# 술 상세페이지 id로 조회
@Liquor.route('/<int:liquor_id>')
class liquor_detailPage(Resource):
    @Liquor.response(200, "Liquor exist", liquor_detail_response)
    @Liquor.response(404, "Not found")
    @Liquor.response(500, "Liquor doesn't exist")
    @Liquor.marshal_with(liquor_detail_response, mask=False)
    def get(self,liquor_id):
        '''술 id로 술 정보 조회'''
        return liquorService.liquor_detail_view(liquor_id)

# 칵테일 상세페이지 id로 조회
@Cocktail.route('/<int:cocktail_id>')
class cocktail_detailPage(Resource):
    @Cocktail.response(200, "Available cocktail_id",cocktail_detail_response)
    @Cocktail.response(404, "Not found")
    @Cocktail.response(500, "Unavailable cocktail_id")
    @Cocktail.marshal_with(cocktail_detail_response , mask=False)
    def get(self,cocktail_id):
        '''칵테일 id로 정보 조회'''
        return liquorService.cocktail_detail_view(cocktail_id)

# 칵테일 레시피 등록 요청
@Cocktail.route('/recipe/create')
# @login_required
class cocktail_recipe(Resource):
    @Cocktail.expect(image_and_recipe)
    @Cocktail.response(201, "recipe successfully created")
    @Cocktail.response(500, "Fail to create")
    def post(self):
        '''유저가 칵테일 레시피 등록'''
        thumbnail = request.files
        data = request.form
        return liquorService.create_cocktail_recipe(thumbnail, data)

# 칵테일 레시피 수정 요청
@Cocktail.route('/recipe/update/<int:user_id>/cocktail/<int:cocktail_id>')
# @login_required
class cocktail_recipe(Resource):
    @Cocktail.expect(image_and_recipe)
    @Cocktail.response(200, "cocktail recipe successfully updated")
    @Cocktail.response(500, "Fail to update")
    def put(self,user_id, cocktail_id):
        '''유저가 칵테일 레시피 수정'''
        thumbnail = request.files
        data = request.form
        return liquorService.update_cocktail_recipe(user_id, cocktail_id, thumbnail, data)

# 칵테일 레시피 삭제 요청
@Cocktail.route('/recipe/delete/<int:user_id>/cocktail/<int:cocktail_id>')
# @login_required
class cocktail_recipe(Resource):
    @Cocktail.response(200, "cocktail recipe successfully deleted")
    @Cocktail.response(500, "Fail to delete")
    def delete(self, user_id, cocktail_id):
        '''유저가 칵테일 레시피 삭제 요청'''
        return liquorService.delete_cocktail_recipe(user_id, cocktail_id)

'''
흔히 204를 반환하는 경우는 PUT 요청에 대한 응답으로, 
사용자에게 보여지는 페이지를 바꾸지 않고 리소스를 업데이트할 때 쓰입니다. 
리소스를 생성한 경우엔 201 Created를 대신 반환합니다. 
새롭게 업데이트한 페이지를 보여줘야 할 경우 200을 사용해야 합니다.
'''