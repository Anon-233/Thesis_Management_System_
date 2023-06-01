from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from . import db

class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key = True, unique = True)
    sender_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable = False
    )
    paper_id = db.Column(
        db.Integer, db.ForeignKey('paper.id'), nullable = False
    )
    content = db.Column(db.Text(), nullable = False)
    time = db.Column(
        db.DateTime(), nullable = False, default = db.func.current_timestamp()
    )

    @classmethod
    def create(cls, sender_id: int, paper_id: int, content: str):
        comment = Comment(
            sender_id = sender_id,
            paper_id = paper_id,
            content = content
        )
        db.session.add(comment)
        db.session.commit()
        return comment

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
        comment_dict = {
            'id': self.id,
            'sender_id': self.sender_id,
            'paper_id': self.paper_id,
            'content': self.content,
            'time': str(self.time)
        }
        return comment_dict

    def __str__(self):
        return str(self.serialize())
