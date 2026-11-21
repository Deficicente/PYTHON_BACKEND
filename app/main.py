from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.models.base import Base
from app.db.session import engine

from app.api.routers.task import router as task_router
from app.api.routers.category import router as category_router

@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=task_router)
app.include_router(router=category_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)











# @app.post("/categories")
# def create_category(payload:CategoryCreate, db: Session = Depends(get_db)) -> Category:
#     new_category = CategoriesORM(title=payload.name)
#     db.add(new_category)
#     db.commit()
#     return category_orm_to_model(new_category)
#
# @app.get("/categories")
# def read_categories(db: Session = Depends(get_db)) -> list[Category]:
#     category_from_db = db.scalars(select(CategoriesORM)).all()
#     return [category_orm_to_model(task) for task in category_from_db]
#
# @app.patch("/categories/{category_id}")
# def update_category(category_id:str, payload:CategoryUpdate, db: Session = Depends(get_db)):
#     category_for_update = db.get(CategoriesORM, category_id)
#
#     if payload.name:
#         category_for_update.name = payload.name
#
#     db.commit()
#
#     return category_for_update
#
# @app.delete("/categories/{category_id}")
# def delete_category(category_id:str, db: Session = Depends(get_db)) -> None:
#     category_for_delete = db.get(CategoriesORM, category_id)
#     db.delete(category_for_delete)
#     db.commit()








