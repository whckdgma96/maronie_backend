from app import db, create_app
from models.liquor import Liquor, Classification

'''
진: 고든스 진, 봄베이 사파이어
럼: 바카디 골드 럼 
위스키: 잭 다니엘, 조니워커 
보드카: 앱솔루트, 스미노프
데킬라: 호세쿠엘보
'''

classfication_sample = Classification(
  classification="Liqueur"
)
db.session.add(classfication_sample)
db.session.commit()

liquor_sample = Liquor(
    liquor_name = "X-Rated",
    image_path = "https://file.mk.co.kr/meet/neds/2020/08/image_readtop_2020_812159_15967844304309365.jpg",
    rating = 4.5,
    description = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum tempora architecto veritatis aliquid ea magni cum libero molestiae facilis maxime dolore odio ipsum natus dignissimos non veniam, quisquam beatae nihil!",
    classification_id = 1
)

db.session.add(liquor_sample)
db.session.commit()