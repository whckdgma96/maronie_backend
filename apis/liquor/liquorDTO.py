from flask_restx import Namespace, fields
from werkzeug.datastructures import FileStorage

Liquor = Namespace(name='Liquor', description='Liquor')
Cocktail = Namespace(name='cocktail', description='Cocktail')

'''custom fields'''
class String2List(fields.Raw):
    def format(self, value):
        return value.split('\\n')

class TotalCount(fields.Raw):
    def format(self, value):
        return len(value)

class RatingDistribution(fields.Raw):
    def format(self, value):
        # distribution={1 : 0, 2:0, 3:0, 4:0, 5:0}
        # distribution[int(value)] +=1
        print(value)
        return 'hi'



recipe_detail = Cocktail.model('recipe_detail',{
    'author_id' : fields.Integer(description='레시피를 등록한 유저의 id', required=True, example=4),
    'cocktail_name': fields.String(description='Cocktail name', required=False, example='Mojito'),
    'cocktail_name_kor': fields.String(description='Cocktail name(Korean)', required=True, example='모히토'),
    'classification_id' : fields.Integer(description='칵테일이 어떤 종류인지', required=True, example=2),
    'level' : fields.Integer(description='난이도',required=False, example=3),
    'alcohol': fields.Float(description='도수', required=False, example=20),
	'description': fields.String(description='Description', required=True, example='오렌지 껍질술인 트리플 섹에 파란 색소를 첨가하여 만든 리큐르. 오렌지 향에 강한 단맛.'),
    'ingredients': String2List(description='재료',required=True, attribute='ingredients', 
                    example=['3 mint leaves',
                    '1/2 ounce simple syrup',
                    '2 ounces white rum',
                    '3/4 ounce lime juice, freshly squeezed',
                    'Club soda, to top',
                    'Garnish: mint sprig',
                    'Garnish: lime wheel']),
    'recipe': String2List(description='레시피',required=True, attribute='recipe', 
                    example=["Lightly muddle the mint with the simple syrup in a shaker.",
                    "Add the rum, lime juice and ice, and give it a brief shake.",
                    "Strain into a highball glass over fresh ice.",
                    "Top with the club soda.",
                    "Garnish with a mint sprig and lime wheel."])
})

'''detail : 상세페이지'''
detail_liquor = Liquor.model('detail_liquor', {
    'liquor_name': fields.String(description='Liquor name', required=True, example='Blue Curacao'),
    'liquor_name_kor': fields.String(description='Liquor name(Korean)', required=True, example='블루 큐라소'),
    'alcohol' : fields.Float(description='도수', required=False, example=20),
    'price': fields.Integer(description='Liquor Price', required=False, example=20000),
    'classification_id' : fields.Integer(description='술이 어떤 종류인지', required=True, example=1),
    'liquor_image': fields.String(description='Image Path', required=False, attribute='image_path', example='https://www.berevita.com/pub/media/catalog/product/cache/image/1000x1320/e9c3970ab036de70892d86c6d221abfe/d/e/de-kuyper-blue-curacao.jpg'),
    'description': fields.String(description='Description', required=True, example='오렌지 껍질술인 트리플 섹에 파란 색소를 첨가하여 만든 리큐르. 오렌지 향에 강한 단맛.'),
    'rating': fields.Float(description='average rating', required=False, example=4.5),
    'total_bookmark' : TotalCount(description='총 즐겨찾기 수',required=True, attribute='wish_l',example=3),
    'total_done' : TotalCount(description='총 마셔봤어요 수',required=True, attribute='done_l', example=3),
    'total_reviews' : TotalCount(description='총 리뷰 수',required=True, attribute='liquor_reviews', example=3),
    # 'distribution' : RatingDistribution(attribute='liquor_reviews'),
})

detail_paring = Liquor.model('detail_paring', {
    'menu_name' : fields.String(description='menu name', required=True, attribute='menus.menu_name' ,example='Beef'),
    'menu_image' : fields.String(description='menu image', required=False, attribute='menus.image_path', example='http://t3.gstatic.com/licensed-image?q=tbn:ANd9GcTMC2SJulbimxkaa029WrkGRfClR5Ds81TjYtMsPezaCG1oQu2eRZccpd7F_goyzm3JgSf7bdM90UqJ_OyD_x0')
})

detail_cocktail_summary =  Liquor.model('detail_cocktail_summary', {
    'cocktail_id' : fields.Integer(description='cocktail id', required=True, attribute='id', example=4),
    'cocktail_name': fields.String(description='Cocktail name', required=False, example='Blue Hawaii'),
    'cocktail_name_kor': fields.String(description='Cocktail name(Korean)', required=True, example='블루 하와이'),
    'cocktail_image': fields.String(description='Image Path', required=False, attribute='image_path',example='https://w.namu.la/s/827ac58e595bb28aa551a1d18fcbcf291a3f01890eb07e4efbb8128eb7007bfdfd0ba10794d4a39194af008f5c7b72c9b6e9386da7a4a0227b19b20884c962d2e2078560c76b2e5a608c4f6dd7b203fdadd31739538aeb5af6c2e26f7b7ac14d'),
    'level': fields.Integer(description='난이도',required=True, attribute='level', example=3)
})

detail_user_reviews = Liquor.model('detail_user_reviews',{
    'nickname' : fields.String(description='유저 닉네임', attribute='reviewed_users.nickname', example='CCH'),
    'rating': fields.Float(description='별점',required=True, attribute='liquor_reviews.rating', example=4.2),
    'content' : fields.String(description='리뷰 내용',required=True, attribute='liquor_reviews.content', example='잭다니엘은 언제먹어도 맛있어요'),
    'date' : fields.Date(description='리뷰 작성 날짜', required=False, attribute='liquor_reviews.date', example='2022-03-08')
})

detail_review = Liquor.model('detail_review',{
    # 'distribution' : RatingDistribution(attribute='rating'),
    'nickname' : fields.String(description='유저 닉네임', required=True, attribute='reviewed_users.nickname', example='CCH'),
    'rating': fields.Float(description='별점',required=True,  example=4.2),
    'content' : fields.String(description='리뷰 내용',required=True,  example='잭다니엘은 언제먹어도 맛있어요'),
    'review_date' : fields.Date(description='리뷰 작성 날짜', required=False,  example='2022-03-08')
})


'''request 형태'''
image_and_recipe = Cocktail.parser()
image_and_recipe.add_argument('file', location='files', type=FileStorage)
image_and_recipe.add_argument('author_id', help='4', location='form', required=True, type=int)
image_and_recipe.add_argument('cocktail_name', help='Mojito', location='form')
image_and_recipe.add_argument('cocktail_name_kor', help='모히토', location='form', required=True)
image_and_recipe.add_argument('classification_id', help='2', location='form', required=True)
image_and_recipe.add_argument('level', help='2', location='form', type=int, required=True)
image_and_recipe.add_argument('alcohol', help='20.3', location='form', type=float)
image_and_recipe.add_argument('description', help='설명', location='form', required=True)                
image_and_recipe.add_argument('ingredients', help='재료1\n재료2\n', location='form', required=True)
image_and_recipe.add_argument('recipe', help="레시피1\n레시피2\n", location='form', required=True)

'''recipe : 칵테일 레시피 관련'''
# recipe_detail = Cocktail.model('recipe_detail',{
#     'author_id' : fields.Integer(description='레시피를 등록한 유저의 id', required=True, example=4),
#     'cocktail_name': fields.String(description='Cocktail name', required=False, example='Mojito'),
#     'cocktail_name_kor': fields.String(description='Cocktail name(Korean)', required=True, example='모히토'),
#     'classification_id' : fields.Integer(description='칵테일이 어떤 종류인지', required=True, example=2),
#     'level' : fields.Integer(description='난이도',required=False, example=3),
#     'alcohol': fields.Float(description='도수', required=False, example=20),
# 	'description': fields.String(description='Description', required=True, example='오렌지 껍질술인 트리플 섹에 파란 색소를 첨가하여 만든 리큐르. 오렌지 향에 강한 단맛.'),
#     'ingredients': String2List(description='재료',required=True, attribute='ingredients', 
#                     example=['3 mint leaves',
#                     '1/2 ounce simple syrup',
#                     '2 ounces white rum',
#                     '3/4 ounce lime juice, freshly squeezed',
#                     'Club soda, to top',
#                     'Garnish: mint sprig',
#                     'Garnish: lime wheel']),
#     'recipe': String2List(description='레시피',required=True, attribute='recipe', 
#                     example=["Lightly muddle the mint with the simple syrup in a shaker.",
#                     "Add the rum, lime juice and ice, and give it a brief shake.",
#                     "Strain into a highball glass over fresh ice.",
#                     "Top with the club soda.",
#                     "Garnish with a mint sprig and lime wheel."])
# })

'''최종 response 형태'''
liquor_detail_response =  Liquor.model('detail_result',{
    'liquor' : fields.Nested(detail_liquor),
    'paring' : fields.Nested(detail_paring),
    'cocktail' : fields.Nested(detail_cocktail_summary),
    'review' : fields.Nested(detail_review)
})

cocktail_detail_response = Cocktail.model('cocktail_detail',{
    'cocktail_name': fields.String(description='Cocktail name', required=False, example='Blue Hawaii'),
    'cocktail_name_kor': fields.String(description='Cocktail name(Korean)', required=True, example='블루 하와이'),
    'author' : fields.String(description='칵테일 레시피 등록한 사람', required=True, attribute='author.nickname', example='admin_Maronie'),
    'image_path': fields.String(description='Image Path', required=False, example='https://w.namu.la/s/827ac58e595bb28aa551a1d18fcbcf291a3f01890eb07e4efbb8128eb7007bfdfd0ba10794d4a39194af008f5c7b72c9b6e9386da7a4a0227b19b20884c962d2e2078560c76b2e5a608c4f6dd7b203fdadd31739538aeb5af6c2e26f7b7ac14d'),
    'alcohol': fields.Float(description='도수', required=False, example=20),
    'level': fields.Integer(description='난이도',required=True, example=3),
    'total_bookmark' : TotalCount(description='총 즐겨찾기 수',required=True, attribute='wish_c',example=3),
    'total_done' : TotalCount(description='총 마셔봤어요 수',required=True, attribute='done_c', example=3),
    'description': fields.String(description='설명',required=True, example='색이 예쁘다. 새콤달콤한 맛'),
    'ingredients': String2List(description='재료',required=True, attribute='ingredients', example=['Gin 1 1/2','레몬즙 1oz','설탕시럽 10ml','탄산수']),
    'recipe': String2List(description='레시피',required=True, attribute='recipe', example=["허리케인 글라스에 얼음", "쉐이커에 얼음", "화이트럼 1oz", "블루큐라소 1/2oz", "파인애플주스 1oz", "라임즙 1/3oz", "Shake", "잔에 부어준다"])
})

