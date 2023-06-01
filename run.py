# pip freeze > ./requirements.txt  
from flask import jsonify
from flask_cors import CORS

from app import create_app
from config import config

environment = config['devlopment']
# environment = config['production']

app = create_app(environment)
CORS(app, supports_credentials=True)
cors = CORS(app)
cors.init_app(app, resource = {
    r'/*': {'origins': '*'}
})

@app.route(rule='/')
def home():
    return '你为什么要访问这里[恼]'

if __name__ == '__main__':
    app.run()