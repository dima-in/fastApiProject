from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel
from typing import Optional
from datetime import date
import requests

app = FastAPI()


class HotelsSearchArgs:
    """
    Класс для хранения параметров GET запроса отелей.
    Request with GET/HEAD method cannot have body.
    """

    def __int__(self,
                location: str,
                date_from: date,
                date_to: date,
                stars: Optional[int] = None,
                has_spa: Optional[bool] = Query(None, ge=1, le=5),
                ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa


@app.get("/hotels/")
def get_hotels(search_args: HotelsSearchArgs = Depends()):
    """
    API эндпоинт, отдает отели
    TODO настроить валидацию
    """

    return search_args


class SBooking(BaseModel):
    """
    SchemaBooking
    описание полей  для передачи в POST запросе
    из формы на странице
    """
    room_id: int
    date_from: date
    date_to: date


@app.post("bookings")
def add_bookings(booking: SBooking):
    pass

# r = requests.get("http://127.0.0.1:8000/hotels/16", params={"date_from": "today", "date_to": "tomorrow"})
