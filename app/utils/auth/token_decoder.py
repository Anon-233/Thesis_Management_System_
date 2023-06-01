import jwt

from config import JWT_SECRET_KEY

def token_decoder(token_enc: str):
    try:
        token_dec = jwt.decode(token_enc, key = JWT_SECRET_KEY, algorithms = 'HS256')
        if token_dec.get('id') is not None:
            return True, token_dec.get('id')
    except:
        return False, -1
