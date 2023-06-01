from flask import Blueprint, request

from ..utils.responses import *

from ..models import db
from ..models.paper import Paper

paper_handler = Blueprint(
    name = 'paper_handler',
    import_name = __name__,
    url_prefix = '/api/paper'
)

@paper_handler.route(rule = '/', methods = ['POST'])
def create_paper():
    data = request.get_json(force = True)
    title = data.get('title', None)
    author = data.get('author', None)
    country = data.get('country', None)
    press = data.get('press', None)
    pressdate = data.get('pressdate', None)
    url = data.get('url', None)
    creater_id = data.get('creater_id', None)
    library_id = data.get('library_id', None)

    paper = Paper.create(
        title = title,
        author = author,
        country = country,
        press = press,
        pressdate = pressdate,
        url = url,
        creater_id = creater_id,
        library_id = library_id
    )
    if paper is None:
        return bad_request(msg = 'DataBase Error, Please Try Again')
    return response_ok(data = paper.serialize())

@paper_handler.route(rule = '/', methods = ['GET'])
def get_paper():
    data = request.get_json(force = True)
    library_id = data.get('library_id', None)
    page_num = data.get('page_num', 0)
    page_size = data.get('page_size', 10)
    if library_id is None:
        return bad_request(msg = 'Missing Field(s)')
    papers = Paper.query.filter(
        Paper.library_id == library_id
    ).offset(page_num * page_size).limit(page_size)
    page_total = Paper.query.count()
    data = [paper.serialize() for paper in papers]
    ret = {'page_total': page_total, 'data': data}
    return response_ok(data = ret)

@paper_handler.route(rule = '/search', methods = ['GET'])
def search_paper():
    pass

@paper_handler.route(rule = '/<paper_id>', methods = ['PUT'])
def update_paper(paper_id):
    pass

@paper_handler.route(rule = '/<paper_id>', methods = ['DELETE'])
def delete_paper(paper_id):
    pass
