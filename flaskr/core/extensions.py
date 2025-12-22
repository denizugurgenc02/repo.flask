from datetime import datetime, timezone
from typing import Any, Generic, List, Optional, Type, TypeVar

from flask import Response, jsonify
from flask.views import MethodView
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, mapped_column


def mapped_foreign_key(target, **kwargs):
    return mapped_column(ForeignKey(target), **kwargs)


class BaseModel(DeclarativeBase):
    pass


class BaseRoutes(MethodView):
    @staticmethod
    def format_response(data: Any, pagination: bool = False) -> Response:
        response = {
            "server_time": datetime.now(timezone.utc).isoformat(),
            "count": len(data) if isinstance(data, list) else 1,
            "items": data if isinstance(data, list) else [data],
        }

        if pagination:
            pass

        return jsonify(response)


T = TypeVar("T")


class BaseRepository(Generic[T]):
    model: Type[T]

    def get_all(self) -> List[T]:
        return list(db.session.execute(select(self.model)).scalars().all())

    def get_by_id(self, item_id: int) -> Optional[T]:
        return db.session.get(self.model, item_id)

    def update(self):
        pass

    def add(self, entity: T) -> T | None:
        try:
            db.session.add(entity)
            db.session.commit()
            return entity
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"{self.model.__name__} can not create. error {e}")
            return None

    def delete(self, entity: T) -> T | None:
        try:
            db.session.delete(entity)
            db.session.commit()
            return entity
        except Exception as e:
            db.session.rollback()
            print(f"{self.model.__name__} can not delete. error {e}")
            return None


db = SQLAlchemy(model_class=BaseModel)
migrate = Migrate()
