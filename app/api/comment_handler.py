from flask import Blueprint, request

from ..utils.responses import *

from ..models import db
from ..models.user import User
from ..models.comment import Comment

comment_handler = Blueprint(
    name = 'comment_handler',
    import_name = __name__,
    url_prefix = '/api/paper'
)

@comment_handler.route(rule = '/comment', methods = ['POST'])
def add_comment():
    data = request.get_json(force = True)
    user_id = data.get('user_id', -1)
    paper_id = data.get('paper_id', -1)
    content = data.get('content', None)
    if user_id == -1 or paper_id == -1 or content is None:
        return bad_request(msg = 'Missing Field(s)')
    comment = Comment.create(
        sender_id = user_id,
        paper_id = paper_id,
        content = content
    )
    return response_ok(data = comment.serialize())

@comment_handler.route(rule = '/comment', methods = ['GET'])
def get_comment():
    data = request.get_json(force = True)
    paper_id = data.get('paper_id', -1)
    page_num = data.get('page_num', 0)
    page_size = data.get('page_size', 10)
    if paper_id == -1:
        return bad_request(msg = 'Missing Field(s)')
    comments = Comment.query.join(User).filter(
        Comment.paper_id == paper_id
    ).with_entities(
        User.username, User.profile_photo, Comment.content, Comment.time
    ).offset(page_num * page_size).limit(page_size)
    ret = [row._asdict() for row in comments]
    return response_ok(data = ret)

@comment_handler.route(rule = '/comment/<comment_id>', methods = ['DELETE'])
def delete_comment(comment_id):
    data = request.get_json(force = True)
    user_id = data.get('user_id', -1)
    if user_id == -1  or paper_id == -1:
        return bad_request(msg = 'Missing Field(s)')
    comment = Comment.query.filter(
        Comment.id == comment_id
    ).first()
    if comment is None:
        return bad_request(msg = 'Invalid Comment ID')
    if comment.sender_id != user_id:
        return bad_request(msg = 'Only the sender can delete it')
    if comment.delete():
        return response_ok(data = comment.serialize())
    return bad_request(msg = 'DataBase Error')
