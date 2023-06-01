from flask import Blueprint, request

from ..utils.responses import *

from ..models import db
from ..models.user import User
from ..models.paper import Paper
from ..models.comment import Comment

comment_handler = Blueprint(
    name = 'comment_handler',
    import_name = __name__,
    url_prefix = '/api/paper'
)

@comment_handler.route(rule = '/comment', methods = ['POST'])
def add_comment():
    data = request.get_json(force = True)
    user_id = data.get('user_id', None)
    paper_id = data.get('paper_id', None)
    content = data.get('content', None)
    if user_id is None or paper_id is None or content is None:
        return bad_request(msg = 'Missing Field(s)')
    user = User.query.filter(
        User.id == user_id
    ).first()
    if user is None:
        return bad_request(msg = 'Invalid User ID')
    paper = Paper.query.filter(
        Paper.id == paper_id
    ).first()
    if paper is None:
        return bad_request(msg = 'Invalid User ID')
    comment = Comment.create(
        sender_id = user_id,
        paper_id = paper_id,
        content = content
    )
    return response_ok(data = comment.serialize())

@comment_handler.route(rule = '/comment/<paper_id>/<page_num>/<page_size>', methods = ['GET'])
def get_comment(paper_id, page_num, page_size):
    paper_id = int(paper_id)
    page_num = int(page_num)
    page_size = int(page_size)
    comments = Comment.query.join(User).filter(
        Comment.paper_id == paper_id
    ).with_entities(
        Comment.id, User.username, User.avatar, Comment.content, Comment.time, Comment.sender_id
    ).order_by(
        Comment.id.desc()
    ).offset(page_num * page_size).limit(page_size)
    ret = [{
        'comment_id': row.id,
        'username': row.username,
        'avatar': row.avatar,
        'content': row.content,
        'time': row.time.strftime('%Y-%m-%d %H:%M:%S'),
        'sender_id': row.sender_id
    } for row in comments]
    return response_ok(data = ret)

@comment_handler.route(rule = '/comment/<comment_id>', methods = ['DELETE'])
def delete_comment(comment_id):
    # data = request.get_json(force = True)
    # user_id = data.get('user_id', None)
    # if user_id is None:
    #     return bad_request(msg = 'Missing Field(s)')
    comment_id = int(comment_id)
    comment = Comment.query.filter(
        Comment.id == comment_id
    ).first()
    if comment is None:
        return bad_request(msg = 'Invalid Comment ID')
    # if comment.sender_id != user_id:
    #     return bad_request(msg = 'Only the sender can delete it')
    if comment.delete():
        return response_ok(data = comment.serialize())
    return bad_request(msg = 'DataBase Error')
