from flaskr.core.base.repository import BaseRepository
from flaskr.domains.category.models import Category


class CategoryRepository(BaseRepository[Category]):
    model = Category
