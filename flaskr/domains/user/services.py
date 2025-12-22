from typing import Any, Dict, List

from flask import abort

from flaskr.domains.user.models import User
from flaskr.domains.user.repositories import UserRepository


class UserService:
    repository = UserRepository()

    def get_by_id(self, item_id: int) -> Any | None:
        user = self.repository.get_by_id(item_id=item_id)

        if user is None:
            abort(404)

        response = user.serialize
        response["role"] = {
            "id": user.role.id,
            "name": user.role.name,
            "created_at": user.role.created_at.isoformat(),
        }
        return response

    def list_users(self) -> List:
        users = self.repository.get_all()
        return [user.serialize for user in users]

    def create_new_user(
        self,
        username: str = None,
        password: str = None,
        display_name: str = None,
        email: str = None,
        role_id: int = None,
    ) -> Dict | None:
        if existing_user := self.repository.get_by_username(username=username):
            abort(
                code=409,
                description=f"this user already current."
                f" detail: {existing_user.serialize}",
            )
        new_user = self.repository.add(
            User(
                username=username,
                password=password,
                display_name=display_name,
                email=email,
                role_id=role_id,
            )
        )
        return new_user.serialize
