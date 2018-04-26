from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import database as database
import jwt_auth

JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 20

app = Flask(__name__)
db = SQLAlchemy(app)
cors = CORS(app, resources={r"/": {"origins": "*"}})

session = []
ORIGIN_VAR = 'localhost'


@app.route('/priv', methods=['GET'])
@cross_origin(origin=ORIGIN_VAR, headers=['Content- Type'])
def priv():
    print("test")
    return jsonify({'message': 'It works!'}), 200


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


@app.route('/dbtest', methods=['GET', 'POST'])
@cross_origin(origin=ORIGIN_VAR, headers=['Content- Type'])
def db_test():
    if request.method == 'POST':
        new_record = {
            'id': request.json['id'],
            'data_text': request.json['data_text']
        }
        new_id = new_record['id']
        new_data_text = new_record['data_text']
        rec_object = database.DBTable(int(new_id), str(new_data_text))
        db.session.add(rec_object)
        db.session.commit()
        return jsonify({'message': 'successful POST send'}), 200

    else:
        db_records = database.DBTable.query.all()
        data_tup = []

        for rec in db_records:
            id_to_send = rec.id
            data_to_send = rec.data_text
            dict_to_send = {'id': id_to_send, 'data_text': data_to_send}
            data_tup.append(dict_to_send)

        return jsonify({'from_db': data_tup}), 200


@app.route('/add_user', methods=['POST'])
@cross_origin(origin=ORIGIN_VAR, headers=['Content- Type'])
def add_user():
    if request.method == 'POST':
        new_user = {
            'username': request.json['username'],
            'password': request.json['password']
        }
        new_username = new_user['username']
        new_password = new_user['password']
        rec_object = database.UsersTable(str(new_username), str(new_password))
        db.session.add(rec_object)
        db.session.commit()
        return jsonify({'message': 'successful POST send'}), 200





