from app.database import Base
from sqlalchemy import JSON, Column, Integer, String
# модель таблицы
class Hotels(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSON)
    room_quantiy = Column(Integer, nullable=False)
    image_id = Column(Integer)

