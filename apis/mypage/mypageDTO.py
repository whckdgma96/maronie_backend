from flask_restx import Namespace,fields

from models.user import Wishlist_cocktail

Mypage = Namespace(name="mypage", description="마이페이지")

wishlist_liquor = Mypage.model('wishlist_liquor',{
    'liquor_id': fields.Integer(description='Liquor id', required=True, example=10, attribute="id"),
    'image_path': fields.String(description='Image Path', required=False, example="https://www.berevita.com/pub/media/catalog/product/cache/image/1000x1320/e9c3970ab036de70892d86c6d221abfe/d/e/de-kuyper-blue-curacao.jpg"),
    'liquor_name_kor':fields.String(description='Liquor name(korean)', required=True, example="블루 큐라소")
})
wishlist_cocktail = Mypage.model('wishlist_cocktail',{
    'cocktail_id': fields.Integer(description='Cocktail id', required=True, example=4, attribute="id"),
    'image_path': fields.String(description='Image Path', required=False, example="https://w.namu.la/s/827ac58e595bb28aa551a1d18fcbcf291a3f01890eb07e4efbb8128eb7007bfdfd0ba10794d4a39194af008f5c7b72c9b6e9386da7a4a0227b19b20884c962d2e2078560c76b2e5a608c4f6dd7b203fdadd31739538aeb5af6c2e26f7b7ac14d"),
    'cocktail_name_kor': fields.String(description='Cocktail name(korean)', required=True, example="블루 하와이"),
})

wishlist_response = Mypage.model('wishlist response',{
    'liquor' : fields.Nested(wishlist_liquor),
    'cocktail' : fields.Nested(wishlist_cocktail)
})

create_wishlist_liquor = Mypage.model('create_wishlist_liquor',{
    'user_id' : fields.Integer(description='user id', required=True, example=2,attribute="user_id"),
    "liquor_id" : fields.Integer(description='liquor id', required=True, example=2,attribute="liquor_id")
})
create_wishlist_cocktail = Mypage.model('create_wishlist_cocktail',{
    'user_id' : fields.Integer(description='user id', required=True, example=2,attribute="user_id"),
    "cocktail_id" : fields.Integer(description='cocktail id', required=True, example=2,attribute="cocktail_id")
})