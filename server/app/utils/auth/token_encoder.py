import jwt
import datetime

from config import JWT_SECRET_KEY

def token_encoder(id: int):
    PERIOD_OF_VALIDITY = 60 # minutes

    JWT_ACCESS_TOKEN_EXPIRES = datetime.datetime.utcnow() + datetime.timedelta(minutes=PERIOD_OF_VALIDITY)
    payload = {
        'id': id,
        'exp': JWT_ACCESS_TOKEN_EXPIRES
    }
    token_enc = jwt.encode(payload = payload, key = JWT_SECRET_KEY, algorithm = 'HS256')
    return token_enc
