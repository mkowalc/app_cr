from flask import request


def get_car_data():

    new_record = {
        'id': request.json['id'],
        'car_name': request.json['car_name'],
        'driver_name': request.json['driver_name'],
        'driver_surname': request.json['driver_surname'],
        'driver_email': request.json['driver_email'],
        'driver_mobile': request.json['driver_mobile'],
        'rent_time': request.json['rent_time'],
        'rent_place': request.json['rent_place'],
        'number_of_days': request.json['number_of_days']
        }
    return new_record
