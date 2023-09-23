from fastapi import APIRouter, HTTPException, status
from fastapi import Response

from app.users.auth import get_password_hash, verify_password, auhtenticate_user, create_access_token
from app.users.dao import UsersDAO
from app.users.schemas import SUserAuth

router = APIRouter(prefix="/auth", tags=["Аутентификация & Пользователи"], )


@router.post("/register")
async def register_user(user_data: SUserAuth):
    """если пользователь с указанным email зарегистрирован, вернем ошибку"""
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await auhtenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    """передаем user.id для аутентификации при передаче токена в запросе """
    access_token = create_access_token({"sub": user.id})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return {"access_token": access_token}


@router.get("/user")
async def get_user():
    user = await UsersDAO.find_one_or_none(id=2)
    return user
