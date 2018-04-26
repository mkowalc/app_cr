import jwt


class JwtAuth(object):

    def __init__(self, auth_header):
        self.auth_header = auth_header

    def decode_auth_token(self, token):
        try:
            payload = jwt.decode(token, 'super-secret-key', algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Login please'
        except jwt.InvalidTokenError:
            return 'Nice try, invalid token. Login please'

    def verify_jwt(self):

        if self.auth_header:
            token = self.auth_header.split(" ")[1]
        else:
            token = ''

        if token:
            decoded = JwtAuth.decode_auth_token(self, token)
            if not isinstance(decoded, str):
                if decoded['name'] == 'admin':
                    return True
                else:
                    return False
            else:
                return False
