from flask import Blueprint, request

from ..utils.responses import *
# from ..models import db
from ..models.user import User
from ..models.library import Library

admin_handler = Blueprint(
    name = 'admin_handler', import_name = __name__, url_prefix = '/api/admin'
)

@admin_handler.route(rule = '/users', methods = ['GET'])
def get_all_users():
    users = User.query.all()
    ret = [user.serialize() for user in users]
    return response_ok(data = ret)

@admin_handler.route(rule = '/librarys', methods = ['GET'])
def get_all_papers():
    librarys = Library.query.all()
    ret = [library.serialize() for library in librarys]
    return response_ok(data = ret)