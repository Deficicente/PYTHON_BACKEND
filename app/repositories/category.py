from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.category import CategoryORM

class CategoryRepository:
    """Ключевые операции с таблицей category в БД"""

    def __init__(self, db:Session):
        self.db = db

    def get_all(self) -> list[CategoryORM]:
        return self.db.scalars(select(CategoryORM)).all()

    def get_by_id(self, category_id:str) -> CategoryORM | None:
        return self.db.get(CategoryORM, category_id)

    def create(self, title:str) -> CategoryORM:
        category = CategoryORM(name=title)
        self.db.add(category)
        return category

    def delete(self, category: CategoryORM):
        self.db.delete(category)