from flaskr.extensions import db
from flaskr.models.user import User


class UserRepository:
    def get_all(self):
        return User.query.all()

    def get_by_id(self, user_id):
        return User.query.get(user_id)

    def add(self, name: str, email: str):
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def delete(self, user: User):
        db.session.delete(user)
        db.session.commit()
        return True
