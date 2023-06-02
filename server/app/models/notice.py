from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from . import db

class Notice(db.Model):
    __tablename__ = 'notice'

    id = db.Column(db.Integer, primary_key = True, unique = True)
    sender_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable = False
    )
    content = db.Column(db.Text(), nullable = False)
    time = db.Column(
        db.DateTime(), nullable = False, default = db.func.current_timestamp()
    )

    @classmethod
    def create(cls, sender_id: int, content: str):
        notice = Notice(
            sender_id = sender_id,
            content = content
        )
        db.session.add(notice)
        db.session.commit()
        return notice

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
        notice_dict = {
            'id': self.id,
            'sender_id': self.sender_id,
            'content': self.content,
            'time': str(self.time).strftime('%Y-%m-%d')
        }
        return notice_dict

    def __str__(self):
        return str(self.serialize())
