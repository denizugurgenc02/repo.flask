from flaskr.repository.user import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.repository = user_repository

    def list_users(self):
        users = self.repository.get_all()
        return [user.serialize for user in users]

    def create_new_user(self, name: str, email: str):

        try:
            new_user = self.repository.add(name, email)
            return new_user.serialize
        except Exception as e:
            print(e)
