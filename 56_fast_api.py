from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    username: str
    age: int


class CreateUser(BaseModel):
    username: str = Field(min_length=5, max_length=20, description="Enter username", examples=["UrbanUser"])
    age: int = Field(ge=18, le=120, description="Enter age", examples=[24])


app = FastAPI()
users: list[User] = []


@app.get("/")
async def main_page() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def user_admin() -> str:
    return "Вы вошли как администратор"


@app.get("/users")
async def get_users() -> list[User]:
    return users


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(ge=1, le=100, description="Enter user ID", example=1)]) -> User:
    for i, u in enumerate(users):
        if u.id == user_id:
            del users[i]
            return u
    raise HTTPException(status_code=404, detail="User was not found")


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(ge=1, le=100, description="Enter user id", example=1)],
        user: CreateUser) -> User:
    for u in users:
        if u.id == user_id:
            u.username = user.username
            u.age = user.age
            return u
    raise HTTPException(status_code=404, detail="User was not found")


@app.post("/user/{username}/{age}", response_model=User)
async def add_user(user: CreateUser) -> User:
    user_id = int(max((u.id for u in users), default=0) + 1)
    new_user = User(id=user_id, username=user.username, age=user.age)
    users.append(new_user)
    return new_user
