
from sqlalchemy import Column, Integer, ForeignKey, String, JSON
from sqlalchemy_json import MutableJson

from app.database import Base

class Rooms(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"))
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)
    services = Column(MutableJson)
    image_id = Column()


