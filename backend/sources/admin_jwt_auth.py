import jwt
import database

#todo
#dodac interfejs/ABC dla klas JwtAuth i AdminJwtAuth

class AdminJwtAuth(object):

    def __init__(self, db, auth_header, secret_key):
        self.db = db
        self.auth_header = auth_header
        self.secret_key = secret_key

    def decode_auth_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return 'Signature expired.'
        except jwt.InvalidTokenError:
            return 'Nice try, invalid token.'

    def get_token(self):

        if self.auth_header:
            token = self.auth_header.split(" ")[1]
            return token
        else:
            token = ''
            return token

    def verify_jwt(self):
        if self.auth_header:
            token = self.get_token()

        if token:
            decoded = self.decode_auth_token(str(token))
            if not isinstance(decoded, str):

                exists = self.db.session.query(
                    self.db.exists().where(
                        (database.AdminTokenTable.admin_token == decoded['admin_token']) and (database.AdminTokenTable.id == decoded['id']))
                    ).scalar()

                if exists:
                    return True

                else:
                    return False
            else:
                return False
        else:
            return False
