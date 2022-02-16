from db_connect import db

class Liquor(db.Model):
    __tablename__ = "liquor"
   
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    liquor_name =db.Column(db.String(100))
    alcohol =db.Column(db.Float, nullable=True)
    price =db.Column(db.Integer, nullable=True)
    image_path =db.Column(db.String(100), nullable=True)
    description =db.Column(db.String(500)) 
    vendor =db.Column(db.String(100), nullable=True)

class Cocktail(db.Model):
    __tablename__ = "cocktail"
   
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cocktail_name =db.Column(db.String(100))
    alcohol =db.Column(db.Float, nullable=True)
    ingredients =db.Column(db.String(100)) 
    recipe =db.Column(db.String(500)) 
    heart =db.Column(db.Integer, default=0)
    level = db.Column(db.Float)
    image_path =db.Column(db.String(100), nullable=True)
    description =db.Column(db.String(500)) 

class Menu(db.Model):
    __tablename__ = "menu"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    menu_name = db.Column(db.String(50))
    image_path =db.Column(db.String(100), nullable=True)

# class Paring(db.Model):
#     __tablename__ = "paring"
#     menu_id = db.Column(db.Integer, db.ForeignKey('menu.id_menu', ondelete='CASCADE', onupdate='CASCADE'))
#     liquor_id = db.Column(db.Integer, db.ForeignKey('menu.id_menu', ondelete='CASCADE', onupdate='CASCADE'))

class Review(db.Model):
    __tablename__ = "review"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'))
    liquor_id = db.Column(db.Integer, db.ForeignKey('liquor.id', ondelete='CASCADE', onupdate='CASCADE'))
    content = db.Column(db.String(200))
    rating = db.Column(db.Float)
    review_date = db.Column(db.Date, nullable=True)

