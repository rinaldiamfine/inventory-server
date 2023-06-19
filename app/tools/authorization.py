from app.user.models import UserModel

def validate_token(headers):
    try:
        header_token = headers.get('authorization')
        token = header_token.split(" ")[1]
        status_decode_uid, decode_uid = UserModel.decode_auth_token(
            auth_token=token
        )
        return status_decode_uid, decode_uid
    except Exception as e:
        return False, str(e)