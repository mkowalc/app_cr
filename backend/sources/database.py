import api as api


db = api.db


class UsersTable(db.Model):
    __tablename__ = 'users'
    username = db.Column('username', db.Unicode, primary_key=True)
    passwd_hash = db.Column('passwd_hash', db.Unicode)

    def __init__(self, username, passwd_hash):
        self.username = username
        self.passwd_hash = passwd_hash


class DBTable(db.Model):
    __tablename__ = 'data'
    id = db.Column('id', db.Integer, primary_key=True)
    data_text = db.Column('data_text', db.Unicode)

    def __init__(self, id, data_text):
        self.id = id
        self.data_text = data_text