from typing import Optional

from sqlalchemy import select

from flaskr.core.extensions import BaseRepository, db
from flaskr.domains.user.models import User


class UserRepository(BaseRepository[User]):
    model = User

    def get_by_username(self, username: str) -> Optional[User]:
        query = select(self.model).filter_by(username=username)
        return db.session.execute(query).scalar_one_or_none()
