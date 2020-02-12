from flask import Flask, url_for, redirect, render_template
from flask import request

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


# website backend bulid up
app = Flask(__name__)
patterns_conn = "mysql+pymysql://root:Root2021@@127.0.0.1:3306/patterns"

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


@app.route('/search/',methods=['GET','POST'])
def search():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
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
	