from typing import List

from flaskr.domains.role.repositories import RoleRepository


class RoleService:
    repository = RoleRepository()

    def list_roles(self) -> List:
        roles = self.repository.get_all()
        return [role.serialize for role in roles]
