import pymysql 

class DataBase():
    def __init__(self):
        pass

    def create_person_date_gps_table(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "patterns" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # Drop table if it already exist using execute() method.
        cursor.execute("drop table if exists person_date_gps")
        # Create table as per requirement
        sql = """create table person_date_gps (
                firstname varchar(20),
                lastname varchar(20),
                carid varchar(10),
                timestamp varchar(200),
                latitude float,
                longtitude float)"""
        cursor.execute(sql)
        # disconnect from server
        db.close()

    def select_person_cc(self, firstname, lastname):
        name = []
        name.append((firstname, lastname))
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "patterns" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select car_assignments.firstname, car_assignments.lastname,
                    car_assignments.carid, cc_data.timestamp, 
                    cc_data.location, cc_data.price
                    from car_assignments, cc_data
                    where car_assignments.firstname = cc_data.firstname
                    and car_assignments.lastname = cc_data.lastname
                    and car_assignments.firstname = %s 
                    and car_assignments.lastname = %s"""
        cursor.executemany(sql, name)
        creditcard_record = cursor.fetchall()
        db.close()
        return creditcard_record

    def select_person_date_gps(self, firstname, lastname, date):
        date = "%" + date + "%"
        person_date = []
        person_date.append((firstname, lastname, date))
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "patterns" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select car_assignments.firstname, car_assignments.lastname,
                    car_assignments.carid, gps.timestamp, gps.lat, gps.long
                    from car_assignments, gps
                    where car_assignments.CarID = gps.id 
                    and firstname = %s
                    and lastname = %s 
                    and timestamp like %s """
        cursor.executemany(sql, person_date)
        person_date_gps = cursor.fetchall()
        sql_insert = """insert into person_date_gps values(%s, %s, %s, %s, %s, %s)"""
        cursor.executemany(sql_insert, person_date_gps)
        db.commit()
        db.close()
        return person_date_gps

    def select_person_loyalty(self, firstname, lastname):
        name = []
        name.append((firstname, lastname))
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "patterns" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select car_assignments.firstname, car_assignments.lastname,
                    car_assignments.carid, loyalty_data.timestamp,
                    loyalty_data.location, loyalty_data.price
                    from car_assignments, loyalty_data
                    where car_assignments.firstname = loyalty_data.firstname
                    and car_assignments.lastname = loyalty_data.lastname
                    and car_assignments.firstname = %s 
                    and car_assignments.lastname = %s"""
        cursor.executemany(sql, name)
        loyalty_record = cursor.fetchall()
        db.close()
        return loyalty_record

    # def select_person_cc_loyalty(self, firstname, lastname):
    #     name = []
    #     name.append((firstname, lastname))
    #     # Open database connection
    #     db = pymysql.connect(user = "root", password = "Root2021@",
    #                         host = "127.0.0.1",
    #                         database = "patterns" )
    #     # prepare a cursor object using cursor() method
    #     cursor = db.cursor()
    #     sql = """select car_assignments.firstname, car_assignments.lastname,
    #                 car_assignments.carid, loyalty_data.timestamp,
    #                 loyalty_data.location, loyalty_data.price,
    #                 cc_data.timestamp, cc_data.location, cc_data.price
    #                 from car_assignments, cc_data, loyalty_data
    #                 where car_assignments.firstname = cc_data.firstname
    #                 and car_assignments.lastname = cc_data.lastname
    #                 and car_assignments.firstname = loyalty_data.firstname
    #                 and car_assignments.lastname = loyalty_data.lastname
    #                 and car_assignments.firstname = %s 
    #                 and car_assignments.lastname = %s"""
    #     cursor.executemany(sql, name)
    #     creditcard_loyalty_record = cursor.fetchall()
    #     db.close()
    #     return creditcard_loyalty_record

    