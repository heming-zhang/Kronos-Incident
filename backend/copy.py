from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


# engine = create_engine("mysql+pymysql://root:Root2021@@127.0.0.1:3306/pok")
# Base = automap_base()
# Base.prepare(engine, reflect = True)
# db = sessionmaker(bind = engine)()
# Article = Base.classes.email
# ret = db.query(Article).first()
# print(ret.emailto)


from flask import Flask, url_for, redirect, render_template
# from flask_sqlalchemy import SQLAlchemy
# import config

app = Flask(__name__)
# # connection with mysql database
# app.config.from_object(config)
# db = SQLAlchemy(app)

# class Article(db.Model):
#     __tablename__ = 'article'
#     id = db.Column(db.Integer, primary_key = True, autoincrement = True)
#     title = db.Column(db.String(100), nullable = Flask)
#     content = db.Column(db.Text, nullable = False)

# class Gps(db.Model):
#     __tablename__ = 'gps'
#     timestamp = db.Column(db.String(255))
#     id = db.Column(db.String(255))
#     latitude = db.Column(db.String(255))
#     longtitude = db.Column(db.String(255))

# db.create_all()

@app.route('/')
def hello_world():
    engine = create_engine("mysql+pymysql://root:Root2021@@127.0.0.1:3306/patterns")
    Base = automap_base()
    Base.prepare(engine, reflect = True)
    db = sessionmaker(bind = engine)()
    Gps = Base.classes.gps
    ret = db.query(Gps).first()
    return ret.timestamp

# @app.route('/')
# def hello_world():
#     article1 = Article(title='aaa',content='bbb')
#     db.session.add(article1)
#     db.session.commit()
#     return 'Hello!'


if __name__ == "__main__":
	app.run(host = "0.0.0.0", debug = True)
	