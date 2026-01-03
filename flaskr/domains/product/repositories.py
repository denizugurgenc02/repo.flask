from flaskr.core.base.repository import BaseRepository
from flaskr.domains.product.models import Product


class ProductRepository(BaseRepository[Product]):
    model = Product
