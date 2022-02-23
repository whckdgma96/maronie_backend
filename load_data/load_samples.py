import os
import pymysql
import dotenv 

dotenv.load_dotenv()

'''
진: 고든스 진, 봄베이 사파이어
럼: 바카디 골드 럼 
위스키: 잭 다니엘, 조니워커 
보드카: 앱솔루트, 스미노프
데킬라: 호세쿠엘보
'''
#타입 확인
# print(type(int(os.environ.get('MYSQL_PORT'))))

conn = pymysql.connect(host='127.0.0.1',
					   port=int(os.getenv('MYSQL_PORT')), 
					   user=os.getenv('MYSQL_USER'),
 					   password=os.getenv('MYSQL_PASSWORD'), 
					   db=os.getenv('MYSQL_DATABASE'), 
					   charset='utf8') 
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

