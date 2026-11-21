from sqlalchemy.orm import Session

from app.repositories.category import CategoryRepository
from app.schemas.category import Category, CategoryCreate, CategoryUpdate

class TaskNotFound(Exception):
    """Задача не напйдена!"""

class CategoryServices:
    def __init__(self, db:Session):
        self.db = db
        self.repository = CategoryRepository(db)

    def list_category(self) -> list[Category]:
        categories = self.repository.get_all()
        return [Category.model_validate(category) for category in categories]

    def create_category(self, payload: CategoryCreate) -> Category:
        category = self.repository.create(title=payload.name)
        self.db.commit()
        return Category.model_validate(category)

    def update_category(self, category_id: str, payload: CategoryUpdate) -> Category:
        category = self.repository.get_by_id(category_id)

        if payload.name is None:
            category.name = payload.name

        self.db.commit()

        return Category.model_validate(category)

    def delete_category(self, category_id:str) -> None:
        category = self.repository.get_by_id(category_id)
        if not category:
            raise TaskNotFound(f"Задача с id {category_id} не найдена!")
        self.repository.delete(category)
        self.db.commit()
