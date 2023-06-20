from app.tools.database import DatabaseManager
import jwt
from datetime import datetime, timedelta
import config

class UserModel:
    def __init__(self):
        self.db = DatabaseManager()
        
    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            expired_token = config.EXPIRED_TOKEN_IN_DAYS
            payload = {
                'exp': datetime.utcnow() + timedelta(days=expired_token),
                'iat': datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                config.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e
    
    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, config.SECRET_KEY, algorithms='HS256')
            return True, payload['sub']
        except jwt.ExpiredSignatureError:
            return False, 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return False, 'Invalid token. Please log in again.'
        
    def auth_users(self, username, password):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE `username` = %s AND `password` = %s", (username, password))
            columns = [column[0] for column in cursor.description]
            result = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
            cursor.close()
            self.db.connection.close()
            if len(result) > 0:
                token = self.encode_auth_token(
                    user_id=result[0].get('id')
                )
                return True, {
                    "message": "Login Success!",
                    "token": token
                }
            else:
                return True, {
                    "message": "Login Failed!",
                    "token": ""
                }
        except Exception as e:
            return False, str(e)
