from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings
RUN_DB_CONTAINER="docker run -d --name my-postgres-container -e POSTGRES_USER=postgresuser -e POSTGRES_PASSWORD=postgrespass -e POSTGRES_DB=postgresdbname -p 5432:5432 postgres"

engine = create_async_engine(settings.DATABASE_URL)

# генератор сессий
assync_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# класс для создания моделей и миграций
class Base(DeclarativeBase):
    pass








