from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import database as database
import jwt_auth
import requests


app = Flask(__name__)
db = SQLAlchemy(app)
cors = CORS(app, resources={r"/": {"origins": "*"}})

session = []
ORIGIN_VAR = 'localhost'


@app.route('/', methods=['GET'])
@cross_origin(origin=ORIGIN_VAR, headers=['Content- Type'])
def test():
    print("test")
    return jsonify({'message': 'It works!'}), 200


@app.route('/auth_test', methods=['GET'])
@cross_origin(origin=ORIGIN_VAR, headers=['Content- Type'])
def test_auth():
    auth_header = request.headers.get('Authorization')
    jwt_auth_test = jwt_auth.JwtAuth(auth_header)
    if jwt_auth_test.verify_jwt():
        return jsonify({'message': 'It works!'}), 200
    else:
        return jsonify({'message': 'error'}), 401


@app.route('/rentacar', methods=['POST'])
@cross_origin(origin=ORIGIN_VAR, headers=['Content- Type'])
def add_car_record():
    auth_header = request.headers.get('Authorization')
    jwt_auth_test = jwt_auth.JwtAuth(auth_header)
    if jwt_auth_test.verify_jwt():
        kwargs = requests.get_car_data()
        car_data = database.CarsDatabase(**kwargs)
        db.session.add(car_data)
        db.session.commit()
        return jsonify({'message': 'successful POST send'}), 200
    else:
        return jsonify({'message': 'error'}), 401

# @app.route('/add_user', methods=['POST'])
# @cross_origin(origin=ORIGIN_VAR, headers=['Content- Type'])
# def add_user():
#     if request.method == 'POST':
#         new_user = {
#             'username': request.json['username'],
#             'password': request.json['password']
#         }
#         new_username = new_user['username']
#         new_password = new_user['password']
#         rec_object = database.UsersTable(str(new_username), str(new_password))
#         db.session.add(rec_object)
#         db.session.commit()
#         return jsonify({'message': 'successful POST send'}), 200





