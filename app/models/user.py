import uuid
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from . import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key = True, unique = True)
    username = db.Column(db.String(32), nullable = False, unique = True)
    password = db.Column(db.String(256), nullable = False)
    avatar = db.Column(db.String(256), nullable = False)
    firstname = db.Column(db.String(32))
    lastname = db.Column(db.String(32))
    birth = db.Column(db.String(32))
    gender = db.Column(db.String(32))
    email = db.Column(db.String(256))
    phone = db.Column(db.String(32))
    location = db.Column(db.String(256))
    available = db.Column(db.Boolean(), nullable = False, default = True)

    MAX_USER_NUM = 10 ** 8

    @classmethod
    def create(
        cls, username: str, password: str, avatar: str = None, firstname: str = None,
        lastname: str = None, birth: str = None, gender: str = None, email: str = None,
        phone: str = None, location: str = None
    ):
        if avatar == '':
            avatar = 'https://qny.littlexi.love/FnY9P71atZdHghxzvBMg4czzwcrY'
        while True:
            try:
                id = int(uuid.uuid4()) % cls.MAX_USER_NUM + 10 ** 9
                user = User(
                    id = id,
                    username = username,
                    password = password,
                    avatar = avatar,
                    firstname = firstname,
                    lastname = lastname,
                    birth = birth,
                    gender = gender,
                    email = email,
                    phone = phone,
                    location = location
                )
                db.session.add(user)
                db.session.commit()
                break
            except db.exc.IntegrityError as e:
                db.session.rollback()
                print(f"Exception occurred during commit: {str(e)}")
        return user

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
        user_dict = {
            'id': self.id,
            'username': self.username,
            'avatar': self.avatar,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'birth': self.birth,
            'gender': self.gender,
            'email': self.email,
            'phone': self.phone,
            'location': self.location
        }
        return user_dict
    
    def __str__(self):
        return str(self.serialize())
