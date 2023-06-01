from flask import Blueprint, request
from sqlalchemy import func

from ..utils.responses import *

from ..models import db
from ..models.user import User
from ..models.library import Library
from ..models.paper import Paper
from ..models.paper_mark import PaperMark
from ..models.comment import Comment

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
    library_title = data.get('library_title', None)
    library_title = str(library_title)

    if title is None or author is None or country is None or press is None or pressdate is None or creater_id is None or library_title is None:
        return bad_request(msg = 'Missing Field(s)')
    user = User.query.filter(
        User.id == creater_id
    ).first
    if user is None:
        return bad_request(msg = 'Invalid User ID')
    library = Library.query.filter(
        Library.title == library_title
    ).first()
    if library is None:
        return bad_request(msg = 'Invalid Library Title')
    library_id = library.id

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

@paper_handler.route(rule = '/<library_id>/<page_num>/<page_size>', methods = ['GET'])
def get_paper(library_id, page_num, page_size):
    library_id = int(library_id)
    page_num = int(page_num)
    page_size = int(page_size)

    papers = Paper.query.filter(
        Paper.library_id == library_id
    ).offset(page_num * page_size).limit(page_size)
    page_total = Paper.query.count()
    data = [paper.serialize() for paper in papers]
    ret = {'page_total': page_total, 'data': data}
    return response_ok(data = ret)

@paper_handler.route(rule = '/click/<paper_id>/<user_id>', methods = ['GET'])
def click_paper(paper_id, user_id):
    paper_id = int(paper_id)
    user_id = int(user_id)
    paper = Paper.query.filter(
        Paper.id == paper_id
    ).first()
    if paper is None:
        return bad_request(msg = 'Invalid Paper ID')
    user = User.query.filter(
        User.id == user_id
    ).first()
    if user is None:
        return bad_request(msg = 'Invalid User ID')

    paper.clicktime = paper.clicktime + 1
    if not paper.commit():
        bad_request(msg = 'DataBase Error, Please Try Again')

    papermark = PaperMark.query.filter(
        PaperMark.marker_id == user_id, PaperMark.paper_id == paper_id
    ).first()
    if papermark is None:
        papermark = PaperMark.create(
            marker_id = user_id,
            paper_id = paper_id,
            mark = 0
        )
    return response_ok(data = papermark.serialize())

@paper_handler.route(rule = '/search', methods = ['GET'])
def search_paper():
    pass

@paper_handler.route(rule = '/<paper_id>', methods = ['PUT'])
def update_paper(paper_id):
    data = request.get_json(force = True)
    title = data.get('title', None)
    author = data.get('author', None)
    country = data.get('country', None)
    press = data.get('press', None)
    pressdate = data.get('pressdate', None)
    url = data.get('url', None)

    paper = Paper.query.filter(
        Paper.id == paper_id
    ).first()
    if paper is None:
        return bad_request(msg = 'Invalid Library ID')
    
    if title is not None:
        paper.title = title
    if author is not None:
        paper.author = author
    if country is not None:
        paper.country = country
    if press is not None:
        paper.press = press
    if pressdate is not None:
        paper.pressdate = pressdate
    if url is not None:
        paper.url = url
    if paper.commit():
        return response_ok(data = paper.serialize())
    return bad_request(msg = 'DataBase Error, Please Try Again')

@paper_handler.route(rule = '/<paper_id>', methods = ['DELETE'])
def delete_paper(paper_id):
    paper = Paper.query.filter(
        Paper.id == paper_id
    ).first()
    if paper is None:
        return bad_request(msg = 'Invalid Library ID')
    
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
    db.session.commit()

    if paper.delete():
        return response_ok(data = paper.serialize())
    return bad_request(msg = 'DataBase Error, Please Try Again')

@paper_handler.route(rule = '/mark', methods = ['POST'])
def mark_paper():
    data = request.get_json(force = True)
    print(data)
    user_id = data.get('user_id', None)
    paper_id = data.get('paper_id', None)
    mark = data.get('mark', None)

    if user_id is None or mark is None or paper_id is None:
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
    
    papermark = PaperMark.query.filter(
        PaperMark.marker_id == user_id
    ).first()
    if papermark is None:
        papermark = PaperMark.create(
            marker_id = user_id,
            paper_id = paper_id,
            mark = mark
        )
    else:
        papermark.mark = mark
        if not papermark.commit():
            return bad_request(msg = 'DataBase Error, Please Try Again')
    
    paper.mark = db.session.query(func.avg(PaperMark.mark)).filter(
        PaperMark.paper_id == paper_id
    ).scalar()
    if paper.commit():
        return response_ok(papermark.serialize())
    return bad_request(msg = 'DataBase Error, Please Try Again')
