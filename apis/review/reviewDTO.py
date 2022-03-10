from flask_restx import Namespace, fields

from apis.review.reviewService import show_review

Review = Namespace(name="review", description='리뷰')

'''review : 리뷰 생성/수정/조회'''
create_reviewDTO = Review.model('create_review',{
    'user_id' :fields.Integer(description='user_id', required=True, example=2),
    'liquor_id': fields.Integer(description='liquor_id', required=True, example= 10),
    'rating':fields.Float(description='rating', required=True,example=3.5),
    'content': fields.String(description='content', required=True, example='최고의 맛'),
})

update_reviewDTO = Review.model('update_review',{
    'review_id' : fields.Integer(description='review_id', attribtue='id', required=True, example=8),
    'user_id' :fields.Integer(description='user_id', required=True, example=2),
    'rating':fields.Float(description='rating', required=True,example=3.5),
    'content': fields.String(description='content', required=True, example='최고의 맛'),
})

show_reviewDTO = Review.model('show_reivew',{
    'review_id' : fields.Integer(description='review_id', attribute='id', required=True, example=2),
    'user_id' :fields.Integer(description='user_id', required=True, example=2),
    'liquor_id': fields.Integer(description='liquor_id', required=True, example= 10),
    'rating':fields.Float(description='rating', required=True,example=3.5),
    'content': fields.String(description='content', required=True, example='최고의 맛'),
    'review_date' : fields.Date(description='content', example='2022-03-10')
})