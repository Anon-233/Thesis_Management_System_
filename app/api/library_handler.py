from flask import Blueprint, request
from sqlalchemy import or_, and_

from ..utils.responses import *

from ..models import db
from ..models.library import Library
from ..models.user import User
from ..models.paper import Paper
from ..models.paper_mark import PaperMark
from ..models.comment import Comment

library_handler = Blueprint(
    name = 'library_handler',
    import_name = __name__,
    url_prefix = '/api/library'
)

@library_handler.route(rule = '/', methods = ['POST'])
def create_library():
    data = request.get_json(force = True)
    title = data.get('title', None)
    topic = data.get('topic', None)
    description = data.get('description', None)
    is_public = data.get('is_public', None)
    creater_id = data.get('creater_id', None)
    certificate = data.get('certificate', None)
    orgnization_name = data.get('orgnization_name', None)
    orgnization_type = data.get('orgnization_type', None)
    orgnization_url = data.get('orgnization_url', None)

    if title is None or topic is None or creater_id is None:
        return bad_request(msg = 'Missing Field(s)')
    if title.strip() == '' or topic.strip() == '':
        return bad_request(msg = 'Missing Field(s)')
    user = User.query.filter(
        User.id == creater_id
    ).first()
    if user is None:
        return bad_request(msg = 'Invalid User ID')
    library = Library.query.filter(
        Library.title == title
    ).first()
    if library is not None:
        return bad_request(msg = 'Library Already Exist')
    
    library = Library.create(
        title = title,
        topic = topic,
        description = description,
        is_public = is_public,
        creater_id = creater_id,
        certificate = certificate,
        orgnization_name = orgnization_name,
        orgnization_type = orgnization_type,
        orgnization_url = orgnization_url
    )
    if library is None:
        return bad_request(msg = 'DataBase Error, Please Try Again')
    return response_ok(data = library.serialize())

@library_handler.route(rule = '/<page_num>/<page_size>', methods = ['GET'])
def get_library(page_num, page_size):
    page_num = int(page_num)
    page_size = int(page_size)
    librarys = Library.query.order_by(
        Library.id.desc()
    ).offset(page_num * page_size).limit(page_size)
    page_total = Library.query.count()
    data = [library.serialize() for library in librarys]
    ret = {'page_total': page_total, 'data': data}
    return response_ok(data = ret)

@library_handler.route(rule = '/search', methods = ['POST'])
def search_library():
    data = request.get_json(force = True)
    title = data.get('title', None)
    page_num = data.get('page_num', 0)
    page_size = data.get('page_size', 10)
    if title is None:
        return bad_request(msg = 'Missing Field(s)')
    
    librarys = Library.query.filter(
        Library.title.like(f'%{title}%')
    ).offset(page_num * page_size).limit(page_size)
    page_total = Library.query.filter(
        Library.title.like(f'%{title}%')
    ).count()
    data = [library.serialize() for library in librarys]
    ret = {'page_total': page_total, 'data': data}
    return response_ok(data = ret)

# @library_handler.route(rule = '/click/<library_id>', methods = ['GET'])
# def click_library(library_id):
#     library_id = int(library_id)
#     library = Library.query.filter(
#         Library.id == library_id
#     ).first()
#     if library is None:
#         return bad_request(msg = 'Invalid Library ID')

#     library.clicktime = library.clicktime + 1
#     if library.commit():
#         return response_ok(data = library.serialize())
#     return bad_request(msg = 'DataBase Error, Please Try Again')

@library_handler.route(rule = '/<library_id>', methods = ['PUT'])
def update_library(library_id):
    data = request.get_json(force = True)
    title = data.get('title', None)
    topic = data.get('topic', None)
    description = data.get('description', None)
    is_public = data.get('is_public', None)
    certificate = data.get('certificate', None)
    orgnization_name = data.get('orgnization_name', None)
    orgnization_type = data.get('orgnization_type', None)
    orgnization_url = data.get('orgnization_url', None)
    # user_id = data.get('user_id', None)
    # if user_id is None:
    #     return bad_request(msg = 'Missing Field(s)')
    library = Library.query.filter(
        Library.id == library_id
    ).first()
    if library is None:
        return bad_request(msg = 'Invalid Library ID')
    # if library.creater_id != user_id:
    #     return bad_request(msg = 'Only the owner of library can update these information')

    if title is not None:
        library.title = title
    if topic is not None:
        library.topic = topic
    if description is not None:
        library.description = description
    if is_public is not None:
        library.is_public = is_public
    if certificate is not None:
        library.certificate = certificate
    if orgnization_name is not None:
        library.orgnization_name = orgnization_name
    if orgnization_type is not None:
        library.orgnization_type = orgnization_type
    if orgnization_url is not None:
        library.orgnization_url = orgnization_url
    if library.commit():
        return response_ok(data = library.serialize())
    return bad_request(msg = 'DataBase Error, Please Try Again')

@library_handler.route(rule = '/<library_id>', methods = ['DELETE'])
def delete_library(library_id):
    # data = request.get_json(force = True)
    # user_id = data.get('user_id', -1)
    # if user_id == -1:
    #     return bad_request(msg = 'Missing Field(s)')
    library = Library.query.filter(
        Library.id == library_id
    ).first()
    if library is None:
        return bad_request(msg = 'Invalid Library ID')
    # if library.creater_id != user_id:
    #     return bad_request(msg = 'Only the owner of library can delete it')
    papers = Paper.query.filter(
        Paper.library_id == library_id
    ).all()
    for paper in papers:
        paper_id = paper.id
        papermarks = PaperMark.query.filter(
            PaperMark.paper_id == paper_id
        ).all()
        for papermark in papermarks:
            db.session.delete(papermark)
        comments = Comment.query.filter(
            Comment.paper_id == paper_id
        ).all()
        for comment in comments:
            db.session.delete(comment)
        paper.delete()
        db.session.commit()

    if library.delete():
        return response_ok(data = library.serialize())
    return bad_request(msg = 'DataBase Error, Please Try Again')
