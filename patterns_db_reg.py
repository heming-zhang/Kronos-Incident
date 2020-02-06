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





class Cc_data(db.Model):
    __tablename__ = 'cc_data'
    autoid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    timestamp = db.Column(db.String(255))
    location = db.Column(db.String(255))
    price = db.Column(db.String(255))
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))

class Car_assignments(db.Model):
    __tablename__ = 'car_assignments'
    autoid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    lastname = db.Column(db.String(255))
    firstname = db.Column(db.String(255))
    carid = db.Column(db.String(255))
    currentemploymenttype = db.Column(db.String(255))
    currentemploymenttitle = db.Column(db.String(255))

class Gps(db.Model):
    __tablename__ = 'gps'
    autoid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    timestamp = db.Column(db.String(255))
    id = db.Column(db.String(255))
    latitude = db.Column(db.String(255))
    longtitude = db.Column(db.String(255))

class Loyalty_data(db.Model):
    __tablename__ = 'loyalty_data'
    autoid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    timestamp = db.Column(db.String(255))
    location = db.Column(db.String(255))
    price = db.Column(db.String(255))
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))

class PatternsInit():
    def __init__(self):
        pass

    def select_cc(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pattern_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select * from cc_data"""
        cursor.execute(sql)
        creditcard_record_list = cursor.fetchall()
        db.close()
        return creditcard_record_list

    def select_car(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pattern_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select * from car_assignments"""
        cursor.execute(sql)
        car_record_list = cursor.fetchall()
        db.close()
        return car_record_list

    def select_gps(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pattern_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select * from gps"""
        cursor.execute(sql)
        gps_record_list = cursor.fetchall()
        db.close()
        return gps_record_list

    def select_loyalty(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pattern_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select * from loyalty_data"""
        cursor.execute(sql)
        loyalty_record_list = cursor.fetchall()
        db.close()
        return loyalty_record_list


def init_cc_data():
    creaditcard_record_list = PatternsInit().select_cc()
    for cc_record in creaditcard_record_list:
        patterns_cc_data = Cc_data(
                    timestamp = cc_record[0],
                    location = cc_record[1],
                    price = cc_record[2],
                    firstname = cc_record[3],
                    lastname = cc_record[4])
        db.session.add(patterns_cc_data)
        db.session.commit()

def init_car_assigments():
    car_record_list = PatternsInit().select_car()
    for car_record in car_record_list:
        patterns_car_assigments = Car_assignments(
                    lastname = car_record[0],
                    firstname = car_record[1],
                    carid = car_record[2],
                    currentemploymenttype = car_record[3],
                    currentemploymenttitle = car_record[4])
        db.session.add(patterns_car_assigments)
        db.session.commit()

def init_gps():
    gps_record_list = PatternsInit().select_gps()
    for gps_record in gps_record_list:
        patterns_gps = Gps(
                    timestamp = gps_record[0],
                    id = gps_record[1],
                    latitude = gps_record[2],
                    longtitude = gps_record[3])
        db.session.add(patterns_gps)
        db.session.commit()

def init_loyalty_data():
    loyalty_record_list = PatternsInit().select_loyalty()
    for loyalty_record in loyalty_record_list:
        patterns_loyalty_data = Loyalty_data(
                    timestamp = loyalty_record[0],
                    location = loyalty_record[1],
                    price = loyalty_record[2],
                    firstname = loyalty_record[3],
                    lastname = loyalty_record[4])
        db.session.add(patterns_loyalty_data)
        db.session.commit()


if __name__ == "__main__":
    # initialize pok data



    # initialize patterns data
    # init_cc_data()
    # init_car_assigments()
    # init_gps()
    # init_loyalty_data()
    