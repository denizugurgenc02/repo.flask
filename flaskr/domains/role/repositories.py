from flaskr.core.base.repository import BaseRepository
from flaskr.domains.role.models import Role


class RoleRepository(BaseRepository[Role]):
    model = Role
