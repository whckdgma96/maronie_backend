from flask_restx import Namespace, fields

Search = Namespace(name="Search", description="술 라벨 이미지 검색 혹은 술과 칵테일 이름으로 정보 검색")

result_liquor = Search.model('result_liquor', {
    'liquor_id': fields.Integer(description='Liquor id', required=True, example=10, attribute="id"),
    'liquor_name': fields.String(description='Liquor name', required=True, example="Blue Curacao"),
    'liquor_name_kor': fields.String(description='Liquor name(korean)', required=True, example="블루 큐라소"),
    'price': fields.Integer(description='Liquor Price', required=False, example=20000),
    'image_path': fields.String(description='Image Path', required=False, example="https://www.berevita.com/pub/media/catalog/product/cache/image/1000x1320/e9c3970ab036de70892d86c6d221abfe/d/e/de-kuyper-blue-curacao.jpg"),
    'description': fields.String(description='Description', required=True, example="오렌지 껍질술인 트리플 섹에 파란 색소를 첨가하여 만든 리큐르. 오렌지 향에 강한 단맛."),
    'rating': fields.Float(description='ration', required=False, example=4.5),
})

result_cocktail = Search.model('result_cocktail', {
    'cocktail_id': fields.Integer(description='Cocktail id', required=True, example=4, attribute="id"),
    'cocktail_name': fields.String(description='Cocktail name', required=True, example="Blue Hawaii"),
    'cocktail_name_kor': fields.String(description='Cocktail name(korean)', required=True, example="블루 하와이"),
    'image_path': fields.String(description='Image Path', required=False, example="https://w.namu.la/s/827ac58e595bb28aa551a1d18fcbcf291a3f01890eb07e4efbb8128eb7007bfdfd0ba10794d4a39194af008f5c7b72c9b6e9386da7a4a0227b19b20884c962d2e2078560c76b2e5a608c4f6dd7b203fdadd31739538aeb5af6c2e26f7b7ac14d"),
    'description': fields.String(description='Description', required=True, example="색이 예쁘다. 새콤달콤한 맛"),
})

result_text_response = Search.model('result_text',{
    'liquor' : fields.Nested(result_liquor),
    'cocktail' : fields.Nested(result_cocktail)
})
