import api as api


db = api.db


class AdminTokenTable(db.Model):
    __tablename__ = 'admin_creds'
    id = db.Column('id', db.Integer, primary_key=True)
    admin_token = db.Column('admin_token', db.Unicode)

    def __init__(self, id, admin_token):
        self.id = id
        self.admin_token = admin_token


class TokenTable(db.Model):
    __tablename__ = 'session_data'
    id = db.Column('id', db.Integer, primary_key=True)
    user_token = db.Column('user_token', db.Unicode)

    def __init__(self, id, user_token):
        self.id = id
        self.user_token = user_token


class CarsDatabase(db.Model):
    __tablename__ = 'cars'
    id = db.Column('id', db.Integer, primary_key=True)
    car_name = db.Column('car_name', db.Unicode)
    driver_name = db.Column('driver_name', db.Unicode)
    driver_surname = db.Column('driver_surname', db.Unicode)
    driver_email = db.Column('driver_email', db.Unicode)
    driver_mobile = db.Column('driver_mobile', db.Unicode)
    rent_time = db.Column('rent_time', db.Unicode)
    rent_place = db.Column('rent_place', db.Unicode)
    number_of_days = db.Column('number_of_days', db.Integer)

    def __init__(self, id, car_name, driver_name, driver_surname, driver_email, driver_mobile, rent_time, rent_place, number_of_days):
        self.id = id
        self.car_name = car_name
        self.driver_name = driver_name
        self.driver_surname = driver_surname
        self.driver_email = driver_email
        self.driver_mobile = driver_mobile
        self.rent_time = rent_time
        self.rent_place = rent_place
        self.number_of_days = number_of_days
