from flask_restx import Resource
from .reviewDTO import *
from . import reviewService
from flask import request, session,abort
from models.user import User
# 리쿼 리뷰 생성
@Review.route('/create')
class Create_review(Resource):
    @Review.expect(create_reviewDTO)
    @Review.response(200, 'Successfully created a review')
    @Review.response(500, 'Failure creating a review')
    def post(self):
        '''술 리뷰 생성'''
        try:
            logined_user = User.query.filter_by(email=session['login']).first()
            user_id = logined_user.id
            liquor_id = request.json['liquor_id']
            rating = request.json['rating']
            content = request.json['content']
            return reviewService.create_review(user_id,liquor_id,rating,content)
        except:
            abort(500, "리뷰 등록 실패.")