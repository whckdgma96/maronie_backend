from flask_restx import Namespace, fields

Liquor = Namespace(name="Liquor", description="Liquor")
Cocktail = Namespace(name="cocktail", description="Cocktail")

detail_liquor = Liquor.model('detail_liquor', {
    'liquor_name': fields.String(description='Liquor name', required=True, example="Blue Curacao"),
    'liquor_name_kor': fields.String(description='Liquor name(korean)', required=True, example="블루 큐라소"),
    'alcohol' : fields.Float(description='도수', required=False, example=20),
    'price': fields.Integer(description='Liquor Price', required=False, example=20000),
    'classification_id' : fields.Integer(description='술이 어떤 종류인지', required=True, example=6),
    'liquor_image': fields.String(description='Image Path', required=False, attribute="image_path", example="https://www.berevita.com/pub/media/catalog/product/cache/image/1000x1320/e9c3970ab036de70892d86c6d221abfe/d/e/de-kuyper-blue-curacao.jpg"),
    'description': fields.String(description='Description', required=True, example="오렌지 껍질술인 트리플 섹에 파란 색소를 첨가하여 만든 리큐르. 오렌지 향에 강한 단맛."),
    'rating': fields.Float(description='average rating', required=False, example=4.5),
    
})

detail_paring = Liquor.model('detail_paring', {
    'menu_name' : fields.String(description='menu name', required=True, attribute="menus.menu_name" ,example="Beef"),
    'menu_image' : fields.String(description='menu image', required=False, attribute="menus.image_path", example="http://t3.gstatic.com/licensed-image?q=tbn:ANd9GcTMC2SJulbimxkaa029WrkGRfClR5Ds81TjYtMsPezaCG1oQu2eRZccpd7F_goyzm3JgSf7bdM90UqJ_OyD_x0")
})

detail_by_liquor =  Liquor.model('detail_by_liquor', {
    'cocktail_name': fields.String(description='Cocktail name', required=True, attribute="cocktails.cocktail_name", example="Blue Hawaii"),
    'cocktail_name_kor': fields.String(description='Cocktail name(korean)', required=True, attribute="cocktails.cocktail_name_kor", example="블루 하와이"),
    'cocktail image': fields.String(description='Image Path', required=False, attribute="cocktails.image_path",example="https://w.namu.la/s/827ac58e595bb28aa551a1d18fcbcf291a3f01890eb07e4efbb8128eb7007bfdfd0ba10794d4a39194af008f5c7b72c9b6e9386da7a4a0227b19b20884c962d2e2078560c76b2e5a608c4f6dd7b203fdadd31739538aeb5af6c2e26f7b7ac14d"),
})

detail_result_response =  Liquor.model('detail_result',{
    'liquor' : fields.Nested(detail_liquor),
    'paring' : fields.Nested(detail_paring),
    'cocktail' : fields.Nested(detail_by_liquor)
})