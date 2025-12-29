from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flaskr.core.base.model import BaseModel

db = SQLAlchemy(model_class=BaseModel)
migrate = Migrate()
