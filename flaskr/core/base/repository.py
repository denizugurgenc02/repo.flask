from typing import Any, Dict, Generic, List, Optional, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from flaskr.core.extensions import db

T = TypeVar("T")


class BaseRepository(Generic[T]):
    model: Type[T]

    def get_all(self) -> List[T]:
        return list(db.session.execute(select(self.model)).scalars().all())

    def get_by_id(self, item_id: int) -> Optional[T]:
        return db.session.get(self.model, item_id)

    def get_by_name(self, column_name: str, value: Any) -> Optional[T]:
        filter_criteria = {column_name: value}
        query = select(self.model).filter_by(**filter_criteria)
        return db.session.execute(query).one_or_none()

    def update(self, item_id: int, data: Dict) -> bool:
        entity = db.session.get(self.model, item_id)

        for key, value in data.items():
            if hasattr(entity, key) and key != "id":
                setattr(entity, key, value)

        try:
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            print(e)
            return False

    def add(self, entity: T) -> T:
        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, item_id: int) -> bool:
        entity = self.get_by_id(item_id=item_id)
        db.session.delete(entity)
        db.session.commit()

        return True
