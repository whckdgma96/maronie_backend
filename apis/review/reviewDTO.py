from flask_restx import Namespace, fields

Review = Namespace(name="review", description='리뷰')

create_reviewDTO = Review.model('create_review',{
    'user_id' :fields.Integer(description='user_id', required=True, example= 4),
    'liquor_id': fields.Integer(description='liquor_id', required=True, example= 10),
    'rating':fields.Float(description='rating', required=True,example=3.5),
    'content': fields.String(description='content', required=True, example='블루 큐라소 만의 맛이 느껴지네요'),
})

update_reviewDTO = Review.model('create_review',{
    'user_id' :fields.Integer(description='user_id', required=True, example= 4),
    'liquor_id': fields.Integer(description='liquor_id', required=True, example= 10),
    'rating':fields.Float(description='rating', required=True,example=3.5),
    'content': fields.String(description='content', required=True, example='블루 큐라소 만의 맛이 느껴지네요'),
})