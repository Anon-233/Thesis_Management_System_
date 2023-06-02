from flask import Blueprint, request

from ..utils.responses import *

from ..models import db
from ..models.user import User
from ..models.notice import Notice

notice_handler = Blueprint(
    name = 'notice_handler',
    import_name = __name__,
    url_prefix = '/api/notice'
)

@notice_handler.route(rule = '/', methods = ['POST'])
def add_notice():
    data = request.get_json(force = True)
    user_id = data.get('user_id', None)
    content = data.get('content', None)

    user = User.query.filter(
        User.id == user_id
    ).first()
    if user is None:
        return bad_request(msg = 'Invalid User ID')

    notice = Notice.create(
        sender_id = user_id,
        content = content
    )
    return response_ok(data = notice.serialize())

@notice_handler.route(rule = '/', methods = ['GET'])
def get_notice():
    notices = Notice.query.order_by(
        Notice.id.desc()
    ).limit(3)
    ret = [notice.serialize() for notice in notices]
    return response_ok(data = ret)
