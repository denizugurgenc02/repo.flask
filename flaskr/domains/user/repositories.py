from flaskr.core.base.repository import BaseRepository
from flaskr.domains.user.models import User


class UserRepository(BaseRepository[User]):
    model = User
