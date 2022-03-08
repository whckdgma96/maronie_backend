from flask_restx import Namespace, fields

Review = Namespace(name="review", description='리뷰')

create_reviewDTO = Review.model('create_review',{
    'user_id' :fields.Integer(description='user_id', required=True, example=2),
    'liquor_id': fields.Integer(description='liquor_id', required=True, example= 10),
    'rating':fields.Float(description='rating', required=True,example=3.5),
    'content': fields.String(description='content', required=True, example='최고의 맛'),
})

update_reviewDTO = Review.model('create_review',{
    'user_id' :fields.Integer(description='user_id', required=True, example=2),
    'liquor_id': fields.Integer(description='liquor_id', required=True, example= 10),
    'rating':fields.Float(description='rating', required=True,example=3.5),
    'content': fields.String(description='content', required=True, example='최고의 맛'),
})