from flask import Blueprint, request
from sqlalchemy import or_, and_

from ..utils.responses import *

from ..models import db
from ..models.library import Library
from ..models.user import User

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
    cignificent = data.get('cignificent', None)
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
    
    library = Library.create(
        title = title,
        topic = topic,
        description = description,
        is_public = is_public,
        creater_id = creater_id,
        cignificent = cignificent,
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
    librarys = Library.query.offset(page_num * page_size).limit(page_size)
    page_total = Library.query.count()
    data = [library.serialize() for library in librarys]
    ret = {'page_total': page_total, 'data': data}
    return response_ok(data = ret)

@library_handler.route(rule = '/search', methods = ['GET'])
def search_library():
    data = request.get_json(force = True)
    topic = data.get('topic', None)
    title = data.get('title', None)
    page_num = data.get('page_num', 0)
    page_size = data.get('page_size', 10)
    if topic is None:
        return bad_request(msg = 'Missing Field(s)')
    
    librarys = Library.query.filter(
        Library.topic == topic, Library.title.like(f'%{title}%')
    ).offset(page_num * page_size).limit(page_size)
    page_total = Library.query.filter(
        Library.topic == topic, Library.title.like(f'%{title}%')
    ).count()
    data = [library.serialize() for library in librarys]
    ret = {'page_total': page_total, 'data': data}
    return response_ok(data = ret)

@library_handler.route(rule = '/<library_id>', methods = ['PUT'])
def update_library(library_id):
    data = request.get_json(force = True)
    title = data.get('title', None)
    topic = data.get('topic', None)
    description = data.get('description', None)
    is_public = data.get('is_public', None)
    creater_id = data.get('creater_id', None)
    cignificent = data.get('cignificent', None)
    orgnization_name = data.get('orgnization_name', None)
    orgnization_type = data.get('orgnization_type', None)
    orgnization_yrl = data.get('orgnization_yrl', None)
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

    library.title = title
    library.topic = topic
    library.description = description
    library.is_public = is_public
    library.creater_id = creater_id
    library.cignificent = cignificent
    library.orgnization_name = orgnization_name
    library.orgnization_type = orgnization_type
    library.orgnization_yrl = orgnization_yrl
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
    if library.delete():
        return response_ok(data = library.serialize())
    return bad_request(msg = 'DataBase Error, Please Try Again')
