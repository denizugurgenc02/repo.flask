from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column


def mapped_foreign_key(target, **kwargs):
    return mapped_column(ForeignKey(target), **kwargs)


class BaseModel(DeclarativeBase):
    pass
