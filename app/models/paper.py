from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from . import db

class  Paper(db.Model):
    __tablename__ = 'paper'

    id = db.Column(db.Integer, primary_key = True, unique = True)
    title = db.Column(db.String(256), nullable = False)
    author = db.Column(db.String(32), nullable = False)
    country = db.Column(db.String(32), nullable = False)
    press = db.Column(db.String(32), nullable = False)
    pressdate = db.Column(db.String(32), nullable = False)
    url = db.Column(db.String(256), nullable = False)
    creater_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable = False
    )
    library_id = db.Column(
        db.Integer, db.ForeignKey('library.id'), nullable = False
    )

    @classmethod
    def create(
        cls, title: str, author: str, country: str, press: int,
        pressdate: str, url: str, creater_id: int, library_id: int
    ):
        try:
            paper = Paper(
                title = title,
                author = author,
                country = country,
                press = press,
                pressdate = pressdate,
                url = url,
                creater_id = creater_id,
                library_id = library_id
            )
            db.session.add(paper)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            print(f"Exception occurred during commit: {str(e)}")
        return paper

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
        paper_dict = {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'country': self.country,
            'press': self.press,
            'pressdate': self.pressdate,
            'url': self.url,
            'creater_id': self.creater_id,
            'library_id': self.library_id
        }
        return paper_dict

    def __str__(self):
        return str(self.serialize())    
