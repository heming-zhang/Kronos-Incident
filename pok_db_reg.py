from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql 
import config

# connection with mysql database
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
db.create_all()

class Article(db.Model):
    __tablename__ = 'article'
    autoid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    filename = db.Column(db.String(255))
    issuedate = db.Column(db.String(255))
    media = db.Column(db.String(255))
    title = db.Column(db.String(255))
    filecontent = db.Column(db.String(255))

class Email(db.Model):
    __tablename__ = 'email'
    autoid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    emailfrom = db.Column(db.String(1255))
    emailto = db.Column(db.Text)
    date = db.Column(db.String(255))
    subject = db.Column(db.Text)

class Emaildegree(db.Model):
    __tablename__ = 'email'
    autoid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    emaildegree = db.Column(db.String(255))
    emailname = db.Column(db.String(255))

class Emailparse(db.Model):
    __tablename__ = 'email'
    autoid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    emailfrom = db.Column(db.String(1255))
    emailto = db.Column(db.String(2000))
    emaildate = db.Column(db.String(255))
    emailsubject = db.Column(db.Text)


class PokInit():
    def __init__(self):
        pass

    def select_article(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pok_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select * from article"""
        cursor.execute(sql)
        article_list = cursor.fetchall()
        db.close()
        return article_list

    def select_email(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pok_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select * from email"""
        cursor.execute(sql)
        email_list = cursor.fetchall()
        db.close()
        return email_list

    def select_emaildegree(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pok_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select * from emaildegree"""
        cursor.execute(sql)
        emaildegree_list = cursor.fetchall()
        db.close()
        return emaildegree_list

    def select_emailparse(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pok_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select * from emailparse"""
        cursor.execute(sql)
        emailparse_list = cursor.fetchall()
        db.close()
        return emailparse_list


def init_article_data():
    article_list = PokInit().select_article()
    for article in article_list:
        pok_article = Article(
                    filename = article[0],
                    issuedate = article[1],
                    media = article[2],
                    title = article[3],
                    filecontent = article[4])
        db.session.add(pok_article)
        db.session.commit()

def init_email():
    email_list = PokInit().select_email()
    for email in email_list:
        pok_email = Email(
                    emailfrom = email[0],
                    emailto = email[1],
                    date = email[2],
                    subject = email[3])
        db.session.add(pok_email)
        db.session.commit()

def init_emaildegree():
    emaildegree_list = PokInit().select_emaildegree()
    for email_degree in emaildegree_list:
        pok_emaildegree = Emaildegree(
                    emaildegree = email_degree[0],
                    emailname = email_degree[1])
        db.session.add(pok_emaildegree)
        db.session.commit()

def init_emailparse():
    emailparse_list = PokInit().select_emailparse()
    for emailparse in emailparse_list:
        pok_emailparse = Emailparse(
                    emailfrom = emailparse[0],
                    emailto = emailparse[1],
                    emaildate = emailparse[2],
                    emailsubject = emailparse[3)
        db.session.add(pok_emailparse)
        db.session.commit()


if __name__ == "__main__":
    # initialize pok data
    init_email()
    init_article_data()
    init_emaildegree()
    init_emailparse()
    