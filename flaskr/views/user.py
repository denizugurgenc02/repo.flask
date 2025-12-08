from flask import Blueprint, jsonify, request
from flask.views import MethodView

from flaskr.repository.user import UserRepository
from flaskr.services.user import UserService

bp = Blueprint("user", __name__, url_prefix="/users")

user_repo = UserRepository()
user_service = UserService(user_repository=user_repo)


class UserListAPI(MethodView):

    def get(self):
        users_data = user_service.list_users()
        return jsonify(users_data)

    def post(self):
        data = request.get_json()

        if not data or "name" not in data or "email" not in data:
            return jsonify({"error": "empty or wrong data."}), 400

        try:
            new_user = user_service.create_new_user(
                name=data["name"], email=data["email"]
            )
            return jsonify(new_user), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 409  # Conflict
        except Exception:
            return jsonify({"error": "Unknow error"}), 500


bp.add_url_rule(
    "/", view_func=UserListAPI.as_view("user_list"), methods=["GET", "POST"]
)
