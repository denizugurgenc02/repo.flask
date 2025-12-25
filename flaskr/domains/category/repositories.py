from typing import Optional

from sqlalchemy import select

from flaskr.core.extensions import BaseRepository,db

from flaskr.domains.category.models import Category

class CategoryRepository(BaseRepository[Category]):
  model=Category