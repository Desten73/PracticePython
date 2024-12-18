from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()
users = {1: 'Имя: Example, возраст: 18'}


@app.get("/")
async def main_page() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def user_admin() -> str:
    return "Вы вошли как администратор"


@app.get("/users")
async def get_users() -> dict:
    return users


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(ge=1, le=100, description="Enter user ID", example=1)]) -> str:
    if users[user_id]:
        users.pop(user_id)
        return f"The user {user_id} is deleted"
    else:
        raise HTTPException(status_code=404, detail="id not found")


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(ge=1, le=100, description="Enter user id", example=1)],
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]) -> str:
    if users[user_id]:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"The user {user_id} is updated"
    else:
        raise HTTPException(status_code=404, detail="id not found")


@app.post("/user/{username}/{age}")
async def add_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]) -> str:
    user_id = int(max(users.keys()) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"
