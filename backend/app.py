from flask import Flask, url_for, redirect, render_template
from flask import request
from flask import jsonify
from flask_cors import CORS

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from dateutil.parser import parse
from datetime import datetime

# website backend bulid up
app = Flask(__name__)
patterns_conn = "mysql+pymysql://root:Root2021@@127.0.0.1:3306/patterns"


@app.route('/init_person', methods=['GET'])
def init_person():
    engine = create_engine(patterns_conn)
    Base = automap_base()
    Base.prepare(engine, reflect = True)
    db = sessionmaker(bind = engine)()
    Gps = Base.classes.gps
    Car_assignments = Base.classes.car_assignments
    result_list = db.query(Car_assignments).filter(Car_assignments.carid.isnot(None))
    personal_info_list = []
    for result in result_list:
        personal_info = {"carid": result.carid,
                    "firstname" : result.firstname,
                    "lastname" : result.lastname}
        personal_info_list.append(personal_info)
    return jsonify(personal_info_list)

@app.route('/init_time', methods=['GET'])
def init_time():
    date = []
    hour = []
    minute = []
    for d in range(6, 20): date.append(d)
    for h in range(0, 24): hour.append(h)
    for m in range(0, 60): minute.append(m)
    time = {"date" : date, "hour" : hour, "minute" : minute}
    return jsonify(time)


@app.route('/search_gps', methods=['GET','POST'])
def search_gps():
    
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")

    time_start = request.args.get("time_start")
    time_end = request.args.get("time_end")
    time_start = datetime.strptime(time_start, "%y-%m-%d %H:%M")
    time_end = datetime.strptime(time_end, "%y-%m-%d %H:%M")
    print(time_start)
    print(time_end)

    engine = create_engine(patterns_conn)
    Base = automap_base()
    Base.prepare(engine, reflect = True)
    db = sessionmaker(bind = engine)()
    Gps = Base.classes.gps
    Car_assignments = Base.classes.car_assignments

    # search gps data with certain name
    result_list = (db.query(Car_assignments, Gps)
                .join(Car_assignments, Car_assignments.carid == Gps.id)
                .filter_by(firstname = firstname)
                .filter_by(lastname = lastname)
                .filter(Gps.timestamp.between(time_start, time_end)))
    gps_record_list = []
    for result in result_list:
        gps_record = {"timestamp" : result.gps.timestamp,
                    "firstname" : result.car_assignments.firstname,
                    "lastname" : result.car_assignments.lastname,
                    "latitude" : float(result.gps.latitude), 
                    "longtitude" : float(result.gps.longtitude)}
        gps_record_list.append(gps_record)
    # return gps_record_list
    return jsonify(gps_record_list)









@app.route('/')
def hello_world():
    engine = create_engine(patterns_conn)
    Base = automap_base()
    Base.prepare(engine, reflect = True)
    db = sessionmaker(bind = engine)()
    Gps = Base.classes.gps
    result_list = db.query(Gps).filter_by(id ="34")
    gps_record_list = []
    for result in result_list:
        gps_record = {"latitude" : result.latitude, "longtitude" : result.longtitude} 
        gps_record_list.append(gps_record)
    return render_template('index.html', gps_record_list = gps_record_list)


@app.route('/search/', methods=['GET','POST'])
def search():
    firstname = "Isia"
    lastname = "Vann"
    time_start = "2014-01-06 08:00"
    time_end = "2014-01-06 17:00"
    engine = create_engine(patterns_conn)
    Base = automap_base()
    Base.prepare(engine, reflect = True)
    db = sessionmaker(bind = engine)()
    Gps = Base.classes.gps
    Car_assignments = Base.classes.car_assignments
    # search gps data with certain name
    if(firstname is not None and lastname is not None):
        result_list = (db.query(Car_assignments, Gps)
                    .join(Car_assignments, Car_assignments.carid == Gps.id)
                    .filter_by(firstname = firstname)
                    .filter_by(lastname = lastname)
                    .filter(Gps.timestamp.between(time_start, time_end)))
        gps_record_list = []
        for result in result_list:
            gps_record = {"timestamp" : result.gps.timestamp,
                         "latitude" : result.gps.latitude, 
                         "longtitude" : result.gps.longtitude}
            gps_record_list.append(gps_record)
    else:
        result_list = db.query(Gps)
        gps_record_list = []
        for result in result_list:
            gps_record = {"latitude" : result.latitude, "longtitude" : result.longtitude} 
            gps_record_list.append(gps_record)
    return render_template('index.html', gps_record_list = gps_record_list)


if __name__ == "__main__":
	app.run(host = "0.0.0.0", debug = True)
	