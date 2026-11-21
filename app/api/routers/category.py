from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_category_service
from app.schemas.category import Category, CategoryCreate, CategoryUpdate
from app.services.category import TaskNotFound, CategoryServices

router = APIRouter(prefix="/categories", tags=["categories"])

@router.get("")
def get_category(service: CategoryServices = Depends(get_category_service)) -> list[Category]:
    return service.list_category()

@router.post("")
def create_category(
        payload: CategoryCreate,
        service: CategoryServices = Depends(get_category_service),
) -> Category:

    return service.create_category(payload)

@router.patch("/{category_id}")
def update_category(
        category_id: str,
        payload: CategoryUpdate,
        service: CategoryServices = Depends(get_category_service),
) -> Category:
    try:
        return service.update_category(category_id, payload)
    except TaskNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Категория не найдена!",
        )

@router.delete("/{category_id}")
def delete_category(
        category_id: str,
        service: CategoryServices = Depends(get_category_service),
) -> None:
    try:
        service.delete_category(category_id)
    except TaskNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Категория не найдена!"
        )


