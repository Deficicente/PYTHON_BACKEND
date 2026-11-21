from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class CategoryORM(Base):
    __tablename__ = "category"

    name: Mapped[str]
