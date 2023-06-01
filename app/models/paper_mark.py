from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from . import db

class  PaperMark(db.Model):
    __tablename__ = 'paper_mark'

    id = db.Column(db.Integer, primary_key = True, unique = True)
    marker_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable = False
    )
    paper_id = db.Column(
        db.Integer, db.ForeignKey('paper.id'), nullable = False
    )
    mark = db.Column(db.Integer, nullable = False, default = 0)
    mark_date = db.Column(
        db.DateTime(), nullable = False, default = db.func.current_timestamp()
    )

    @classmethod
    def create(cls, marker_id: int, paper_id: int, mark: int):
        try:
            papermark = PaperMark(
                marker_id = marker_id,
                paper_id = paper_id,
                mark = mark
            )
            db.session.add(papermark)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            print(f"Exception occurred during commit: {str(e)}")
        return papermark

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
        papermark_dict = {
            'id': self.id,
            'marker_id': self.marker_id,
            'paper_id': self.paper_id,
            'mark': self.mark,
            'mark_date': self.mark_date.strftime('%Y-%m-%d')
        }
        return papermark_dict

    def __str__(self):
        return str(self.serialize())    
