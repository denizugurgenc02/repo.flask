from enum import Enum


class UserRole(Enum):
    ADMIN = "admin"
    SERVICE_STAFF = "service_staff"
    KITCHEN_STAFF = "kitchen_staff"

    @classmethod
    def list_all(cls):
        return [role.value for role in cls]
