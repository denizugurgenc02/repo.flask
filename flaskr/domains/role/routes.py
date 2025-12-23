from flaskr.core.extensions import BaseRoutes
from flaskr.domains.role.services import RoleService

from . import bp


class RoleListAPI(BaseRoutes):
    service = RoleService()

    def get(self):  # Return all roles
        roles_data = self.service.list_roles()
        return self.format_response(data=roles_data)


bp.add_url_rule("/", view_func=RoleListAPI.as_view("role_list_api"), methods=["GET"])
