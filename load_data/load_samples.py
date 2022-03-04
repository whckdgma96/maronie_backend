import os
import bcrypt
import pymysql
import dotenv 
import pandas as pd

dotenv.load_dotenv()

#타입 확인
# print(type(int(os.environ.get('MYSQL_PORT'))))

#Connecting to the database
conn = pymysql.connect(host='127.0.0.1',
					   port=int(os.getenv('MYSQL_PORT')), 
					   user=os.getenv('MYSQL_USER'),
 					   password=os.getenv('MYSQL_PASSWORD'), 
					   db=os.getenv('MYSQL_DATABASE'), 
					   charset='utf8') 

# Creating a cursor object to execute
cur = conn.cursor()

'''기존 데이터를 모두 지우고 AUTO_INCREMENT도 초기화 한다.'''
cur.execute('''show tables''')
tables = cur.fetchall() #튜플 형태

for table in tables:
	cur.execute(f"DELETE FROM {table[0]}")
	cur.execute(f"ALTER TABLE {table[0]} AUTO_INCREMENT = 1")

# Opening csv files
df_user = pd.read_csv('user_sample.csv',keep_default_na=False)
df_classification = pd.read_csv('classification_sample.csv',keep_default_na=False) #keep_default_na=False : NaN->None로 바꾸기. None은 db에서 null로 인식된다
df_liquor = pd.read_csv('liquor_sample.csv',keep_default_na=False)
df_cocktail = pd.read_csv('cocktail_sample.csv',keep_default_na=False)
df_byLiquor = pd.read_csv('by_liquor_sample.csv',keep_default_na=False)
df_menu = pd.read_csv('menu_sample.csv',keep_default_na=False)
df_paring = pd.read_csv('paring_sample.csv',keep_default_na=False)
df_wishlist_cocktail = pd.read_csv('wishlist_cocktail_sample.csv',keep_default_na=False)
df_wishlist_liquor = pd.read_csv('wishlist_liquor_sample.csv',keep_default_na=False)
df_donelist_cocktail = pd.read_csv('donelist_cocktail_sample.csv',keep_default_na=False)
df_donelist_liquor = pd.read_csv('donelist_liquor_sample.csv',keep_default_na=False)
df_review = pd.read_csv('review_sample.csv',keep_default_na=False, encoding='cp949')

'''user'''
#User 테이블에 id 1번으로 admin 유저 넣기
encrypted_pw = bcrypt.hashpw(os.getenv('ADMIN_USER_PASSWORD').encode('utf-8'),bcrypt.gensalt())
cur.execute('''INSERT INTO user (email, password, nickname) VALUES(%s,%s,%s)''', [os.getenv('ADMIN_USER_EMAIL'), encrypted_pw, "admin_Maronie"])

for row in df_user.itertuples():
	encrypted_pw = bcrypt.hashpw(row.password.encode('utf-8'),bcrypt.gensalt())
	cur.execute('''INSERT INTO user (email, password, nickname) VALUES(%s,%s,%s)''', [row.email, encrypted_pw, row.nickname])

'''classification'''
for row in df_classification.itertuples():
		cur.execute('''INSERT INTO classification (classification) VALUES(%s)''', [row.classification])

'''liquor'''
for row in df_liquor.itertuples():
		cur.execute('''INSERT INTO liquor (liquor_name, liquor_name_kor, classification_id, alcohol, price, image_path, description, rating, vendor) 
		VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)''', [row.liquor_name, row.liquor_name_kor, row.classification_id, row.alcohol, row.price, row.image_path, row.description, row.rating, row.vendor])

'''cocktail'''
#author_id, heart는 default value로 한다.
for row in df_cocktail.itertuples():
		cur.execute('''INSERT INTO cocktail (cocktail_name, cocktail_name_kor, alcohol, image_path, description, level, ingredients, recipe) 
		VALUES(%s,%s,%s,%s,%s,%s,%s,%s)''', [row.cocktail_name, row.cocktail_name_kor, row.alcohol, row.image_path, row.description, row.level, row.ingredients, row.recipe])

'''by_liquor'''
for row in df_byLiquor.itertuples():
		cur.execute('''INSERT INTO by_liquor (classification_id, cocktail_id) 
		VALUES(%s, %s)''', [row.classification_id, row.cocktail_id])

'''menu'''
for row in df_menu.itertuples():
		cur.execute('''INSERT INTO menu (menu_name, image_path) 
		VALUES(%s, %s)''', [row.menu_name, row.image_path])

'''paring'''
for row in df_paring.itertuples():
		cur.execute('''INSERT INTO paring (menu_id, classification_id) 
		VALUES(%s, %s)''', [row.menu_id, row.classification_id])

'''donelist_cocktail'''
for row in df_donelist_cocktail.itertuples():
		cur.execute('''INSERT INTO donelist_cocktail (id, cocktail_id,user_id) 
		VALUES(%s, %s, %s)''', [row.id, row.cocktail_id, row.user_id])

'''donelist_liquor'''
for row in df_donelist_liquor.itertuples():
		cur.execute('''INSERT INTO donelist_liquor (id, liquor_id,user_id) 
		VALUES(%s, %s, %s)''', [row.id, row.liquor_id, row.user_id])

'''wishlist_cocktail'''
for row in df_wishlist_cocktail.itertuples():
		cur.execute('''INSERT INTO wishlist_cocktail (id, cocktail_id,user_id) 
		VALUES(%s, %s, %s)''', [row.id, row.cocktail_id, row.user_id])

'''wishlist_liquor'''
for row in df_wishlist_liquor.itertuples():
		cur.execute('''INSERT INTO wishlist_liquor (id, liquor_id,user_id) 
		VALUES(%s, %s, %s)''', [row.id, row.liquor_id, row.user_id])

'''review'''
for row in df_review.itertuples():
		cur.execute('''INSERT INTO review (id, user_id, liquor_id, rating, content, review_date) 
		VALUES(%s,%s,%s,%s,%s,%s)''', [row.id, row.user_id, row.liquor_id, row.rating, row.content, row.review_date])

#Committing the changes
conn.commit()

#closing the database con
conn.close()

'''
진: 고든스 진, 봄베이 사파이어
럼: 바카디 골드 럼 
위스키: 잭 다니엘, 조니워커 
보드카: 앱솔루트, 스미노프
데킬라: 호세쿠엘보
'''