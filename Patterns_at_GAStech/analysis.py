from pythondb import DataBase

class Analyze():
    def __init__(self):
        pass

    # def creditcard_loyalty_site_search(self):
    #     firstname = "Isia"
    #     lastname = "Vann"
    #     creditcard_loyalty_record = DataBase().select_person_cc_loyalty(firstname, lastname)
    #     for record in creditcard_loyalty_record:
    #         print(record)

    def creditcard_site_search(self):
        firstname = "Isia"
        lastname = "Vann"
        creditcard_record = DataBase().select_person_cc(firstname, lastname)
        for record in creditcard_record:
            print(record)

    def gps_site_search(self):
        firstname = "Isia"
        lastname = "Vann"
        date = "01/06/2014"
        DataBase().create_person_date_gps_table()
        person_date_gps = DataBase().select_person_date_gps(firstname, lastname, date)
        for gps in person_date_gps:
            print(gps)

    def loyalty_site_search(self):
        firstname = "Isia"
        lastname = "Vann"
        loyalty_record = DataBase().select_person_loyalty(firstname, lastname)
        for record in loyalty_record:
            print(record)