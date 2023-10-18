
from .. import db, flask_bcrypt
import datetime
# from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt
from typing import Union


class User():
    """ User Model for storing user related details """
    # __tablename__ = "user"

    @staticmethod
    def encode_auth_token(login, password) -> bytes:

        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'login': login,
                'password': password
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token: str): #-> Union[str, strinint]:

        try:
            payload = jwt.decode(auth_token, key, algorithms=['HS256'])
            # print(payload)
            return payload
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def __repr__(self):
        return "<User '{}'>".format(self.username)
