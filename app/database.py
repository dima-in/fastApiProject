from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DB_HOST = "localhost"
DB_PORT = 5432
DS_USER = "postgresuser"
DB_PASS = "postgrespass"
DB_NAME = "postgresdbname"
RUN_DB_CONTAINER = "docker run -d --name my-postgres-container -e POSTGRES_USER=postgresuser -e POSTGRES_PASSWORD=postgrespass -e POSTGRES_DB=postgresdbname -p 5432:5432 postgres"
DB_URL = f"postgresql+asyncpg://{DS_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DB_URL)

# генератор сессий
assync_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# класс для создания моделей и миграций
class Base(DeclarativeBase):
    pass








