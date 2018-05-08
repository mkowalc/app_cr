from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import database as database
import jwt
import user_jwt_auth
import admin_jwt_auth
import requests
import rand


app = Flask(__name__)
db = SQLAlchemy(app)
cors = CORS(app, resources={r"/": {"origins": "*"}})

session = []
ORIGIN_VAR = 'localhost'
secret_key = 'bla-secret-blah'
admin_secret_key = 'admin-secret'


@app.route('/get_token', methods=['GET'])
@cross_origin(origin=ORIGIN_VAR, headers=['Content- Type'])
def return_jwt():
    user_id = rand.id_generator(5)
    user_token = rand.str_generator(10)
    kwargs = {'id': user_id,
              'user_token': user_token}
    new_usr_payload = database.TokenTable(**kwargs)
    db.session.add(new_usr_payload)
    try:
        db.session.commit()
    finally:
        print("closing")
        db.session.close()
    payload = {
        "id": user_id,
        "user_token": user_token,
    }
    print(payload)
    jwt_token = jwt.encode(payload, secret_key, algorithm='HS256')
    return jsonify({'token': str(jwt_token)}), 200


@app.route('/rentacar', methods=['POST'])
@cross_origin(origin=ORIGIN_VAR, headers=['Content- Type'])
def add_car_record():
    auth_header = request.headers.get('Authorization')
    jwt_auth_test = user_jwt_auth.UserJwtAuth(db, auth_header, secret_key)
    is_jwt_correct = jwt_auth_test.verify_token()
    if is_jwt_correct:
        kwargs = requests.get_car_data()
        car_data = database.CarsDatabase(**kwargs)
        db.session.add(car_data)
        try:
            db.session.commit()
        finally:
            print("closing car session")
            db.session.close()
        return jsonify({'message': 'successful POST send'}), 200
    else:
        return jsonify({'message': 'error'}), 401


@app.route('/secreturl', methods=['GET'])
@cross_origin(origin=ORIGIN_VAR, headers=['Content- Type'])
def get_cars_records():
    auth_header = request.headers.get('Authorization')
    jwt_auth_admin = admin_jwt_auth.AdminJwtAuth(db, auth_header, admin_secret_key)
    is_jwt_correct = jwt_auth_admin.verify_token()
    if is_jwt_correct:
        db_records = database.CarsDatabase.query.all()
        data_tup = []

        for record in db_records:
            dict_to_send = {
                'id': record.id,
                'car_name': record.car_name,
                'driver_name': record.driver_name,
                'driver_surname': record.driver_surname,
                'driver_email': record.driver_email,
                'driver_mobile': record.driver_mobile,
                'rent_time': record.rent_time,
                'rent_place': record.rent_place,
                'number_of_days': record.number_of_days
            }

            data_tup.append(dict_to_send)

        return jsonify({'from_db': data_tup}), 200
    else:
        return jsonify({'message': 'error'}), 401






