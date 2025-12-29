from flaskr.core.base.services import BaseService
from flaskr.domains.role.repositories import RoleRepository


class RoleService(BaseService):
    repository: RoleRepository
    repository = RoleRepository()
