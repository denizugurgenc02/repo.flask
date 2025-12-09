from flask import Blueprint

from . import routes  # noqa F401

bp = Blueprint("user", __name__, url_prefix="/users")
