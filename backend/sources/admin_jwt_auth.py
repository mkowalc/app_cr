import jwt
import database
import abstract_jwt_auth


class AdminJwtAuth(abstract_jwt_auth.AbstractJwtAuth):

    def decode_token(self, token):
        return super().decode_token(token)

    def get_token(self):
        return super().get_token()

    def verify_token(self):
        if self.auth_header:
            token = self.get_token()

        if token:
            decoded = self.decode_token(str(token))
            if not isinstance(decoded, str):

                exists = self.db.session.query(
                    self.db.exists().where(
                        (database.AdminTokenTable.admin_token == decoded['admin_token']) and (database.AdminTokenTable.id == decoded['id']))
                    ).scalar()
                self.db.session.close()

                if exists:
                    return True

                else:
                    return False
            else:
                return False
        else:
            return False
