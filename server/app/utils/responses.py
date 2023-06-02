from flask import jsonify

def bad_request(msg: str = 'Bad Request'):
    ret = {
        'success': False,
        'data': {},
        'message': msg,
        'code': 400
    }
    return jsonify(ret), 400

def response_ok(data):
    ret  = {
        'success': True,
        'data': data,
        'message': '',
        'code': 200
    }
    return jsonify(ret), 200

def not_found(msg: str = 'Resource not Found'):
    ret = {
        'success': False,
        'data': {},
        'message': msg,
        'code': 404
    }
    return jsonify(ret), 404
