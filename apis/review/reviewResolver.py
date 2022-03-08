from flask_restx import Resource
from .reviewDTO import *
from . import reviewService
from flask import request, session,abort
from models.user import User
# 리쿼 리뷰 생성
@Review.route('/create')
class Create_review(Resource):
    @Review.expect(create_reviewDTO)
    @Review.response(201, '리뷰등록 성공')
    @Review.response(500, 'Failed to create a review')
    def post(self):
        '''술 리뷰 생성'''

        user_id = request.json['user_id']
        liquor_id = request.json['liquor_id']
        rating = request.json['rating']
        content = request.json['content']
        return reviewService.create_review(user_id,liquor_id,rating,content)


@Review.route('/update')
class UpdateReview(Resource):
    @Review.expect(update_reviewDTO)
    @Review.response(200, 'Review revision successful')
    @Review.response(500, 'Failed to revise the review')
    def post(self):
        '''술 리뷰 수정'''
        user_id = request.json['user_id']
        liquor_id = request.json['liquor_id']
        rating = request.json['rating']
        content = request.json['content']
        return reviewService.update_review(user_id,liquor_id,rating,content)
