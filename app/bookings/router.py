from fastapi import APIRouter, Request, Depends

from app.bookings.dao import BookingsDAO
from app.bookings.schemas import SBookings
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(prefix="/bookings", tags=["Бронирования"], )


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user())): # -> list[SBookings]:

    return await BookingsDAO.find_all()


@router.get("/find_one_or_none")
async def get_bookings():
    booking = await BookingsDAO.find_one_or_none(room_id=1)
    return booking
