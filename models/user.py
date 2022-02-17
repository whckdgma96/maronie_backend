from db_connect import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, nullable=False, auto_increment=True)
    email = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(255), nullable=False)
    nickname = db.Column(db.String(45), nullable=False)

def init_db(): #to-do) 따로 파일로 빼기
    db.create_all()
    
if __name__ == '__main__':
    init_db()