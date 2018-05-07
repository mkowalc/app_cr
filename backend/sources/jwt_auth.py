import jwt


class JwtAuth(object):

    def __init__(self, auth_header, secret_key):
        self.auth_header = auth_header
        self.secret_key = secret_key

    def decode_auth_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Login please'
        except jwt.InvalidTokenError:
            return 'Nice try, invalid token. Login please'

    def get_token(self):

        if self.auth_header:
            token = self.auth_header.split(" ")[1]
            return token
        else:
            token = ''
            return token
    #przekazac obiekt bd do tej funkcji, jak się da!
    # def verify_jwt(self):
    #
    #     if self.auth_header:
    #         token = self.auth_header.split(" ")[1]
    #     else:
    #         token = ''
    #
    #     if token:
    #         decoded = JwtAuth.decode_auth_token(self, token)
    #         if not isinstance(decoded, str):
    #             if (decoded['id'] == self.id) and (decoded['user_token'] == self.user_token):
    #                 return True
    #             else:
    #                 return False
    #         else:
    #             return False
