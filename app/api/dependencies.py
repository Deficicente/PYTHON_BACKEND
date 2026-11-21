from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.task import TaskServices
from app.services.category import CategoryServices


def get_task_service(db: Session = Depends(get_db)):
    """Функция для инъекции зависимости TaskServices"""
    return TaskServices(db)

def get_category_service(db: Session = Depends(get_db)):
    return CategoryServices(db)