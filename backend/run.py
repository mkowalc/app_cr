from sources.api import app


if __name__ == '__main__':
    db_localisation = 'mysql+pymysql://app-user:PASSWORD@localhost/db_app'
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['SECRET_KEY'] = 'super-secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_localisation
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_COOKIE_CSRF_PROTECT'] = True
    app.run(host='0.0.0.0', debug=True)
