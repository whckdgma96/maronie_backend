from flask_restx import Namespace, fields

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

'''detail : 술 상세페이지의 리뷰 더보기 기능'''
detail_reviews = Review.model('detail_reviews',{
    'nickname' : fields.String(description='유저 닉네임', required=True, attribute='reviewed_users.nickname', example='CCH'),
    'rating': fields.Float(description='별점',required=True,  example=4.2),
    'content' : fields.String(description='리뷰 내용',required=True,  example='잭다니엘은 언제먹어도 맛있어요'),
    'review_date' : fields.Date(description='리뷰 작성 날짜', required=False,  example='2022-03-08')
})

next_reviewsDTO = Review.model('next_reviews',{
    'last_review_id' : fields.Integer(describe='보낸 리뷰의 마지막 리뷰의 아이디', required=True, example=23),
    'liquor_id' : fields.Integer(description='liquor_id', required=True, example= 17),
    'reviews' : fields.Nested(detail_reviews)
})