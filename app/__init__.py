from flask import Flask

from .models  import db

from .api.admin_handler import admin_handler
from .api.auth_handler import auth_handler
from .api.library_handler import library_handler
from .api.paper_handler import paper_handler
from .api.comment_handler import comment_handler
from .api.notice_handler import notice_handler

from .models.user import init_user_db

app = Flask(__name__)

def init_db():
    init_user_db()

def create_app(environment):
    app.config.from_object(environment)

    app.register_blueprint(admin_handler)
    app.register_blueprint(auth_handler)
    app.register_blueprint(library_handler)
    app.register_blueprint(paper_handler)
    app.register_blueprint(comment_handler)
    app.register_blueprint(notice_handler)

    with app.app_context():
        db.init_app(app)
        db.drop_all()
        db.create_all()

        init_db()

        return app
    return None