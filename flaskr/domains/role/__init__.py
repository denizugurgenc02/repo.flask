from flask import Blueprint

bp = Blueprint("role", __name__, url_prefix="/roles")

from . import routes  # noqa F401
