from flask import Blueprint, request
import hashlib

from ..utils.auth.token_encoder import token_encoder
from ..utils.auth.token_decoder import token_decoder
from ..utils.responses import *
from ..models import db
from ..models.user import User

auth_handler = Blueprint(
    name = 'auth_handler', import_name = __name__, url_prefix = '/api/user'
)

@auth_handler.route(rule = '/login', methods = ['POST'])
def auth_login():
    data = request.get_json(force = True)
    username = data.get('username', None)
    password = data.get('password', None)

    if username is None or password is None:
        return bad_request(msg = 'Missing Field(s)')
    hash_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    user = User.query.filter(
        User.username == username, User.password == hash_password
    ).first()
    if user is None:
        return bad_request(msg = 'Invalid Username or Password')
    if user.available == False:
        return bad_request(msg = 'User Logged Out!')
    
    token_enc = token_encoder(id = user.id)
    ret = dict(user.serialize(), **{'token': token_enc})
    return response_ok(data = ret)

@auth_handler.route(rule = '/token', methods = ['POST'])
def auth_token():
    data = request.get_json(force = True)
    token_enc = data.get('token', None)

    if token_enc is None:
        return bad_request(msg = 'Empty Token')
    success, id = token_decoder(token_enc = token_enc)
    if not success:
        return bad_request(msg = 'Invalid Token')
    user = User.query.filter(
        User.id == id
    ).first()
    if user is None:
        return bad_request(msg = 'Invalid Token')
    if user.available == False:
        return bad_request(msg = 'User Logged Out!')
    
    return response_ok(data = user.serialize())

@auth_handler.route(rule = '/register', methods = ['POST'])
def auth_register():
    data = request.get_json(force = True)
    username = data.get('username', None)
    password = data.get('password', None)
    avatar = data.get('avatar', None)
    firstname = data.get('firstname', None)
    lastname = data.get('lastname', None)
    birth = data.get('birth', None)
    gender = data.get('gender', None)
    email = data.get('email', None)
    phone = data.get('phone', None)
    location = data.get('location', None)

    if username is None or password is None:
        return bad_request(msg = 'Missing Field(s)')
    if username.strip() == '' or password.strip() == '':
        return bad_request(msg = 'Missing Field(s)')
    user = User.query.filter(
        User.username == username
    ).first()
    if user is not None:
        return bad_request(msg = 'Username Already Exists')

    hash_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    user = User.create(
        username = username,
        password = hash_password,
        avatar = avatar,
        firstname = firstname,
        lastname = lastname,
        birth = birth,
        gender = gender,
        email = email,
        phone = phone,
        location = location
    )
    token_enc = token_encoder(user.id)
    ret = dict(user.serialize(), **{'token': token_enc})
    return response_ok(data = ret)

@auth_handler.route(rule = '/modify', methods = ['PUT'])
def modify_user():
    data = request.get_json(force = True)
    id = data.get('id', None)
    avatar = data.get('avatar', None)
    firstname = data.get('firstname', None)
    lastname = data.get('lastname', None)
    birth = data.get('birth', None)
    gender = data.get('gender', None)
    email = data.get('email', None)
    phone = data.get('phone', None)
    location = data.get('location', None)

    user = User.query.filter(
        User.id == id
    ).first()
    if user is None:
        return bad_request(msg = 'Invalid User ID')

    if avatar is not None:
        user.avatar = avatar
    if firstname is not None:
        user.firstname = firstname
    if lastname is not None:
        user.lastname = lastname
    if birth is not None:
        user.birth = birth
    if gender is not None:
        user.gender = gender
    if email is not None:
        user.email = email
    if phone is not None:
        user.phone = phone
    if location is not None:
        user.location = location
    if user.commit():
        return response_ok(data = user.serialize())
    return bad_request(msg = 'DataBase Error, Please Try Again')

@auth_handler.route(rule = '/change', methods = ['PUT'])
def change_password():
    data = request.get_json(force = True)
    id = data.get('id', None)
    oldpassword = data.get('oldpassword', None)
    newpassword = data.get('newpassword', None)

    hash_oldpassword = hashlib.sha256(oldpassword.encode('utf-8')).hexdigest()
    hash_newpassword = hashlib.sha256(newpassword.encode('utf-8')).hexdigest()
    user = User.query.filter(
        User.id == id
    ).first()
    if user is None:
        return bad_request(msg = 'Invalid User ID')
    if user.password != hash_oldpassword:
        return bad_request(msg = 'Invalid Password')
    
    user.password = hash_newpassword
    if user.commit():
        return response_ok(data = user.serialize())
    return bad_request(msg = 'DataBase Error, Please Try Again')


@auth_handler.route(rule = '/delete', methods = ['PUT'])
def delete_user():
    data = request.get_json(force = True)
    id = data.get('id', None)

    user = User.query.filter(
        User.id == id
    ).first()
    if user is None:
        return bad_request(msg = 'Invalid User ID')
    if user.available == False:
        return bad_request(msg = 'User Logged Out!')

    user.available = False
    if user.commit():
        return response_ok(data = user.serialize())
    return bad_request(msg = 'DataBase Error, Please Try Again')

