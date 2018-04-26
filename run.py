from sources.api import app


if __name__ == '__main__':
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['SECRET_KEY'] = 'super-secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/mkow/Desktop/app_backend/sources/db/db_app.db'
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_COOKIE_CSRF_PROTECT'] = True
    app.run(host='0.0.0.0', debug=True)
