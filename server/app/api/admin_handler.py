from flask import Blueprint, request

from ..utils.responses import *
# from ..models import db
from ..models.user import User
from ..models.library import Library
from ..models.paper import Paper
from ..models.comment import Comment

admin_handler = Blueprint(
    name = 'admin_handler', import_name = __name__, url_prefix = '/api/admin'
)

@admin_handler.route(rule = '/users', methods = ['GET'])
def get_all_users():
    users = User.query.all()
    ret = [user.serialize() for user in users]
    return response_ok(data = ret)

@admin_handler.route(rule = '/librarys', methods = ['GET'])
def get_all_librarys():
    librarys = Library.query.all()
    ret = [library.serialize() for library in librarys]
    return response_ok(data = ret)

@admin_handler.route(rule = '/papers', methods = ['GET'])
def get_all_papers():
    papers = Paper.query.all()
    ret = [paper.serialize() for paper in papers]
    return response_ok(data = ret)

@admin_handler.route(rule = '/comments', methods = ['GET'])
def get_all_comments():
    comments = Comment.query.all()
    ret = [comment.serialize() for comment in comments]
    return response_ok(data = ret)