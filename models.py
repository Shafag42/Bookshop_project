from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from pymysql import NULL
from extensions import db,login_manager
from app import app
class genre(db.Model):
    __tablename__="genre"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255),nullable=False)
    def __repr__(self):
        return f'{self.name}'
    def __init__(self,name):
        self.name=name
    def save(self):
        db.session.add(self)
        db.session.commit()
class language(db.Model):
    __tablename__="language"
    id=db.Column(db.Integer,primary_key=True)
    lang_code=db.Column(db.String(2),nullable=False)
    lang_name=db.Column(db.String(255),nullable=False)
    def __repr__(self):
        return f'{self.lang_name}'
    def __init__(self,lang_code,lang_name):
        self.lang_code=lang_code
        self.lang_name=lang_name
    def save(self):
        db.session.add(self)
        db.session.commit()
class books(db.Model):
    __tablename__="books"
    id = db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255),unique=True)
    author=db.Column(db.String(255),nullable=False)
    description=db.Column(db.Text,nullable=True,default=NULL)
    price=db.Column(db.Float,default=10.00)
    image_url=db.Column(db.Text)
    stock=db.Column(db.Integer)
    genre=db.Column(db.Integer,db.ForeignKey('genre.id'),nullable=False)
    language_id=db.Column(db.Integer,db.ForeignKey('language.id'),nullable=False)
    publisher=db.Column(db.String(255))
    def __repr__(self):
        return f'{self.title}'
    def __init__(self,title,author,description,price,image_url,stock,genre,language_id,publisher):
        self.title=title
        self.author=author
        self.description=description
        self.price=price
        self.image_url=image_url
        self.stock=stock
        self.genre=genre
        self.language_id=language_id
        self.publisher=publisher
    def save(self):
        db.session.add(self)
        db.session.commit()
class Comments(db.Model):
    __tablename__ = "Comments"
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(30), nullable = False)
    comment = db.Column(db.Text, nullable = False)
    date_of_comment = db.Column(db.DateTime)
    book_id=db.Column(db.ForeignKey(books.id),nullable=False)
    def __repr__(self):
        return self.full_name
    def __init__(self, full_name, comment, date_of_comment,book_id):
        self.full_name = full_name
        self.comment = comment
        self.date_of_comment = date_of_comment
        self.book_id=book_id
    def save(self):
        db.session.add(self)
        db.session.commit()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(30), nullable = False, unique = True)
    username = db.Column(db.String(30), nullable = False, unique = True)
    password = db.Column(db.String(255), nullable = False)
    is_active = db.Column(db.Boolean, default = True)
    is_superuser = db.Column(db.Boolean, default = True)
    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)
    def save(self):
        db.session.add(self)
        db.session.commit()
    def check_password(self, password):
        return check_password_hash(self.password, password)