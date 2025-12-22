from flaskr.core.extensions import BaseRepository
from flaskr.domains.role.models import Role


class RoleRepository(BaseRepository[Role]):
    model = Role
