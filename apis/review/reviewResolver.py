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
        # try:
        # logined_user = User.query.filter_by(email=session['login']).first()
        # user_id = logined_user.id
        if not session:
            abort(500, "로그인 해주세요")
        else:
            user_id = request.json['user_id']
            liquor_id = request.json['liquor_id']
            rating = request.json['rating']
            content = request.json['content']
            return reviewService.create_review(user_id,liquor_id,rating,content)
        # except:
        #     abort(500, "리뷰 등록 실패.")

@Review.route('/update')
class Update_review(Resource):
    @Review.expect(update_reviewDTO)
    @Review.response(200, 'Review revision successful')
    @Review.response(500, 'Failed to revise the review')
    def post(self):
        '''술 리뷰 수정'''
        if not session:
            abort(500, "로그인 해주세요")
        else:
            review_id = request.json['review_id']
            user_id = request.json['user_id']
            rating = request.json['rating']
            content = request.json['content']
            return reviewService.update_review(user_id,review_id,rating,content)
        # except:
        #     abort(500, "로그인 해주세요.")

@Review.route("/delete/<int:review_id>/user/<int:user_id>")
class delete_review(Resource):
    def delete(self, user_id, review_id):
        '''등록된 리뷰 삭제'''
        if not session:
            abort(500, "로그인 해주세요")
        else:
            return reviewService.delete_review( user_id, review_id)

@Review.route("/<int:review_id>/user/<int:user_id>")
class review(Resource):
    @Review.response(200, "Review exist",show_reviewDTO)
    @Review.response(500, "Review doesn't exist")
    @Review.marshal_with(show_reviewDTO, mask=False)
    def get(self, user_id, review_id):
        '''리뷰 하나만 조회'''
        return reviewService.get_review(user_id, review_id)

@Review.route("/liquor/<int:liquor_id>/more_reviews/<int:last_review_id>")
class next_reviews(Resource):
    @Review.response(200, "Review exist",next_reviewsDTO)
    @Review.response(500, "Review doesn't exist")
    @Review.marshal_with(next_reviewsDTO, mask=False)
    def get(self, liquor_id, last_review_id):
        '''다음 리뷰 불러오기'''
        return reviewService.get_next_reviews(liquor_id, last_review_id)