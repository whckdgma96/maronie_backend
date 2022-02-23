import pymysql
# from app import db, create_app
# from models.liquor import Liquor, Classification

'''
진: 고든스 진, 봄베이 사파이어
럼: 바카디 골드 럼 
위스키: 잭 다니엘, 조니워커 
보드카: 앱솔루트, 스미노프
데킬라: 호세쿠엘보
'''

conn = pymysql.connect(host='127.0.0.1',port=3306, user='team11', password='AIteam11Liquor', db='Liquor', charset='utf8') #숨기기
cur = conn.cursor()

#기존 데이터를 모두 지우고 AUTO_INCREMENT도 초기화 한다.
cur.execute('''DELETE FROM liquor''')
cur.execute('''DELETE FROM classification''')
cur.execute('''ALTER TABLE classification AUTO_INCREMENT = 1''')
cur.execute('''ALTER TABLE liquor AUTO_INCREMENT = 1''')
cur.execute('''INSERT INTO classification (classification) VALUES("Liqueur")''')

#Committing the changes
conn.commit()

cur.execute('''INSERT INTO liquor (liquor_name, classification_id, image_path, rating, description) VALUES(%s,%s,%s,%s,%s)''', 
	["X-Rated", 1, "https://file.mk.co.kr/meet/neds/2020/08/image_readtop_2020_812159_15967844304309365.jpg", 4.5, "abc"])

#Committing the changes
conn.commit()

#closing the database con
conn.close()


# classfication_sample = Classification(
#   classification="Liqueur"
# )
# db.session.add(classfication_sample)
# db.session.commit()

# liquor_sample = Liquor(
#     liquor_name = "X-Rated",
#     image_path = "https://file.mk.co.kr/meet/neds/2020/08/image_readtop_2020_812159_15967844304309365.jpg",
#     rating = 4.5,
#     description = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum tempora architecto veritatis aliquid ea magni cum libero molestiae facilis maxime dolore odio ipsum natus dignissimos non veniam, quisquam beatae nihil!",
#     classification_id = 1
# )

# db.session.add(liquor_sample)
# db.session.commit()