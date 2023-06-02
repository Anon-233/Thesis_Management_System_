from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy import func

from . import db

class Library(db.Model):
    __tablename__ = 'library'

    id = db.Column(db.Integer, primary_key = True, unique = True)
    title = db.Column(db.String(32), nullable = False, unique = True)
    topic = db.Column(db.String(256), nullable = False)
    description = db.Column(db.Text())
    is_public = db.Column(db.Boolean(), nullable = False, default = False)
    creater_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable = False
    )
    certificate = db.Column(db.String(256))
    orgnization_name = db.Column(db.String(32))
    orgnization_type = db.Column(db.String(32))
    orgnization_url = db.Column(db.String(256))
    clicktime = db.Column(db.Integer, nullable = False, default = 0)
    papernumber = db.Column(db.Integer, nullable = False, default = 0)
    created_date = db.Column(
        db.DateTime(), nullable = False, default = db.func.current_timestamp()
    )


    @classmethod
    def create(
        cls, title: str, topic: str, description: str, is_public: bool, creater_id: int, 
        certificate: str, orgnization_name: str, orgnization_type: str, orgnization_url: str
    ):
        library = None
        try:
            library = Library(
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
            db.session.add(library)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            print(f"Exception occurred during commit: {str(e)}")
        return library

    def commit(self):
        try:
            db.session.commit()
            return True
        except (SQLAlchemyError, IntegrityError) as e:
            db.session.rollback()
            print(f"Exception occurred during commit: {str(e)}")
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except (SQLAlchemyError, IntegrityError) as e:
            db.session.rollback()
            print(f"Exception occurred during commit: {str(e)}")
            return False
    
    def serialize(self):
        library_dict = {
            'id': self.id,
            'title': self.title,
            'topic': self.topic,
            'description': self.description,
            'is_public': self.is_public,
            'creater_id': self.creater_id,
            'certificate': self.certificate,
            'orgnization_name': self.orgnization_name,
            'orgnization_type': self.orgnization_type,
            'orgnization_url': self.orgnization_url,
            'clicktime': self.clicktime,
            'papernumber': self.papernumber,
            'created_date': self.created_date.strftime('%Y-%m-%d')
        }
        return library_dict
    
    def __str__(self):
        return str(self.serialize())
    
