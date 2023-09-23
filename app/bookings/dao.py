from app.bookings.models import Bookings
from dao.base import BaseDAO

"""BookingsDAO наследуется от BaseDAO и конкретизирует базовый функционал для работы с моделью Bookings"""

class BookingsDAO(BaseDAO):
    model = Bookings


