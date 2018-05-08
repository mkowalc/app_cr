import jwt
from abc import ABC, abstractmethod


class AbstractJwtAuth(ABC):

    def __init__(self, db, auth_header, secret_key):
        self.db = db
        self.auth_header = auth_header
        self.secret_key = secret_key

    @abstractmethod
    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return 'Signature expired.'
        except jwt.InvalidTokenError:
            return 'Nice try, invalid token.'

    @abstractmethod
    def get_token(self):

        if self.auth_header:
            token = self.auth_header.split(" ")[1]
            return token
        else:
            token = ''
            return token

    def verify_token(self):
        pass
