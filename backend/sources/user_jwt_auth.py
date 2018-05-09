import abstract_jwt_auth
import database


class UserJwtAuth(abstract_jwt_auth.AbstractJwtAuth):

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
                        (database.TokenTable.user_token == decoded['user_token']) and (database.TokenTable.id == decoded['id']))
                    ).scalar()
                self.db.session.close()

                if exists:
                    #todo

                    return True

                else:
                    return False

            else:
                return False

        else:
            return False

    def delete_token(self):

        if self.auth_header:
            token = self.get_token()
            print("test1")

        if token:
            print("Test2")
            decoded = self.decode_token(str(token))
            if not isinstance(decoded, str):
                self.db.session.close()
                jwt_token = database.TokenTable.query.filter(database.TokenTable.id == decoded['id']).first()
                print(jwt_token)
                self.db.session.delete(jwt_token)
                self.db.session.commit()
                self.db.session.close()
