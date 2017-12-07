from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////bd-data/prueba.db'
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////Users/ratakas/Documents/docker/app/database/prueba.db'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////root/Documents/python/app/database/prueba.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db=SQLAlchemy(app)


class exploit(db.Model):
	__tablename__='exploit'
	id = db.Column(db.String(512), primary_key=True)
	category_id = db.Column(db.Integer)
	title = db.Column(db.String(512))
	url = db.Column(db.Text)
	content = db.Column(db.Text)
	#timestrap = db.Column(db.String(512))
	timestrap = db.Column(db.DateTime)
	#timepost = db.Column(db.String(512))
	timepost = db.Column(db.DateTime)
	category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))
	category = db.relationship('category',backref=db.backref('exploits', lazy='dynamic'))

	def __init__(self, id,category_id, title,url,content,timestrap=None,timepost=None):
		self.id = id
		self.category_id = category_id
		self.title = title
		self.url = url
		self.content = content
		self.timestrap = timestrap
		self.timepost = timepost
	
	def __repr__(self):
		return '<title %r>' % self.title

class category(db.Model):
	__tablename__='category'
	category_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))

	def __init__(self, category_id,name):
		self.category_id = category_id
		self.name = name

	def __repr__(self):
		return '<Category %r>' % self.name

db.create_all()

file = db.session.query(category).filter_by(category_id=1).first()
if file== None:
	me=category(category_id=1,name='Exploit')
	db.session.add(me)
file = db.session.query(category).filter_by(category_id=2).first()
if file== None:
	me=category(category_id=2,name='Advisory')
	db.session.add(me)
file = db.session.query(category).filter_by(category_id=3).first()
if file== None:
	me=category(category_id=3,name='Tool')
	db.session.add(me)

db.session.commit()
db.session.close()
