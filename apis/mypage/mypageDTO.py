from flask_restx import Namespace,fields

'''custom fields'''
class String2List(fields.Raw):
    def format(self, value):
        return value.split('\\n')

Mypage = Namespace(name="mypage", description="마이페이지")

wishlist_liquor = Mypage.model('wishlist_liquor',{
    'id' : fields.Integer(description='wishlist_liquor id', required=True, example=1,attribute="id"),
    'liquor_id': fields.Integer(description='Liquor id', required=True, example=10, attribute="wish_l_info.id"),
    'image_path': fields.String(description='Image Path', attribute='wish_l_info.image_path', required=False, example="https://www.berevita.com/pub/media/catalog/product/cache/image/1000x1320/e9c3970ab036de70892d86c6d221abfe/d/e/de-kuyper-blue-curacao.jpg"),
    'liquor_name_kor':fields.String(description='Liquor name(korean)', attribute='wish_l_info.liquor_name_kor', required=True, example="블루 큐라소")
})
wishlist_cocktail = Mypage.model('wishlist_cocktail',{
    'id' : fields.Integer(description='wishlist_cocktail id', required=True, example=1,attribute="id"),
    'cocktail_id': fields.Integer(description='Cocktail id', required=True, example=4, attribute="wish_c_info.id"),
    'image_path': fields.String(description='Image Path', attribute='wish_c_info.image_path', required=False, example="https://w.namu.la/s/827ac58e595bb28aa551a1d18fcbcf291a3f01890eb07e4efbb8128eb7007bfdfd0ba10794d4a39194af008f5c7b72c9b6e9386da7a4a0227b19b20884c962d2e2078560c76b2e5a608c4f6dd7b203fdadd31739538aeb5af6c2e26f7b7ac14d"),
    'cocktail_name_kor': fields.String(description='Cocktail name(korean)', attribute='wish_c_info.cocktail_name_kor', required=True, example="블루 하와이"),
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


donelist_liquor = Mypage.model('donelist_liquor',{
    'id' : fields.Integer(description='donelist_liquor id', required=True, example=1,attribute="id"),
    'liquor_id': fields.Integer(description='Liquor id', required=True, example=10, attribute="done_l_info.id"),
    'image_path': fields.String(description='Image Path', attribute='done_l_info.image_path', required=False, example="https://www.berevita.com/pub/media/catalog/product/cache/image/1000x1320/e9c3970ab036de70892d86c6d221abfe/d/e/de-kuyper-blue-curacao.jpg"),
    'liquor_name_kor':fields.String(description='Liquor name(korean)', attribute='done_l_info.liquor_name_kor', required=True, example="블루 큐라소")
})
donelist_cocktail = Mypage.model('donelist_cocktail',{
    'id' : fields.Integer(description='donelist_cocktail id', required=True, example=1,attribute="id"),
    'cocktail_id': fields.Integer(description='Cocktail id', required=True, example=4, attribute="done_l_info.id"),
    'image_path': fields.String(description='Image Path', attribute='done_c_info.image_path', required=False, example="https://w.namu.la/s/827ac58e595bb28aa551a1d18fcbcf291a3f01890eb07e4efbb8128eb7007bfdfd0ba10794d4a39194af008f5c7b72c9b6e9386da7a4a0227b19b20884c962d2e2078560c76b2e5a608c4f6dd7b203fdadd31739538aeb5af6c2e26f7b7ac14d"),
    'cocktail_name_kor': fields.String(description='Cocktail name(korean)', attribute='done_c_info.cocktail_name_kor', required=True, example="블루 하와이"),
})

donelist_response = Mypage.model('donelist response',{
    'liquor' : fields.Nested(donelist_liquor),
    'cocktail' : fields.Nested(donelist_cocktail)
})

create_donelist_liquor = Mypage.model('create_donelist_liquor',{
    'user_id' : fields.Integer(description='user id', required=True, example=2,attribute="user_id"),
    "liquor_id" : fields.Integer(description='liquor id', required=True, example=2,attribute="liquor_id")
})
create_donelist_cocktail = Mypage.model('create_donelist_cocktail',{
    'user_id' : fields.Integer(description='user id', required=True, example=2,attribute="user_id"),
    "cocktail_id" : fields.Integer(description='cocktail id', required=True, example=2,attribute="cocktail_id")
})

my_cocktail_recipe = Mypage.model('my_cocktail_recipe',{

    'cocktail_id' : fields.Integer(description='칵테일 id', required=True, example=1,attribute="id"),
    'author_id' : fields.Integer(description='레시피를 등록한 유저의 id',required=True, example=1),
    'cocktail_name': fields.String(description='Cocktail name', required=False, example='Black Russian'),
    'cocktail_name_kor': fields.String(description='Cocktail name(Korean)', required=True, example='블랙 러시안'),
    'image_path': fields.String(description='Image Path', required=False, example='https://stevethebartender.com.au/ezoimgfmt/m8g5e5y2.stackpathcdn.com/wp-content/uploads/2014/07/black-russian-cocktail.jpg?ezimgfmt=ng:webp/ngcb1'),
    'level' : fields.Integer(description='난이도',required=False, example=1),
    'alcohol': fields.Float(description='도수', required=False, example=37.9),
	'description': fields.String(description='Description', required=True, example='커피향과 술 맛을 동시에 느낄 수 있지만 도수가 상당히 높은 칵테일'),
    'ingredients': String2List(description='재료',required=True, attribute='ingredients', 
                    example=['Vodka 50ml\nKahlúa 20ml']),
    'recipe': String2List(description='레시피',required=True, attribute='recipe', 
                    example=['온더락잔에 얼음\n보드카 50ml\n깔루아 20ml\nStir'])
})

my_review = Mypage.model('my_review',{
    'review_id' : fields.Integer(description='review_id',required=True, example=1,attribute="id"),
    'liquor_id' : fields.Integer(description='liquor_id',required=True,example=8,attribute='liquor_id'),
    "liquor_name": fields.String(description='liquor_name',required=True,example='Blue Curacao',attribute='reviewed_liquors.liquor_name'),
    "liquor_name_kor" :fields.String(description='liquor_name_kor',required=True,example='블루 큐라소',attribute='reviewed_liquors.liquor_name_kor'),
    'image_path': fields.String(description='Image Path', required=False,example='media/thumbnail_liquor/0bbc5579-ede9-4c4e-b4d5-a9fb97bf1eb3.jpg',attribute='reviewed_liquors.image_path'),
    'rating' : fields.Float(description='rating',required=True,example=4.5,attribute='rating'),
    'content': fields.String(description='content',required=True,example='블루 큐라소 만의 맛이 느껴지네요',attribute='content'),
    "review_date" : fields.Date(description='review_date',required=False,example='2022-02-03')
})