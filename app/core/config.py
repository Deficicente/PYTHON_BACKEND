#импортируем декоратор для быстрого создания классов для хранения
from dataclasses import dataclass

#используем декоратор и устанавливаем значение frozen=True, делая его неизменяемым
@dataclass(frozen=True)
class Settings:
    DATABASE_URL:str
    cors_allowed_origins: list[str]

#для работы с FastAPI и зависимостями получаем объекта класса через функцию
def get_settings() -> Settings:
    return Settings(
        DATABASE_URL="postgresql+psycopg://postgres:admin@127.0.0.1:5432/postgres",
        cors_allowed_origins=["http://localhost:3000"]
    )