from fastapi import FastAPI, Path, HTTPException, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    username: str
    age: int


class CreateUser(BaseModel):
    username: str = Field(min_length=5, max_length=20, description="Enter username", examples=["UrbanUser"])
    age: int = Field(ge=18, le=120, description="Enter age", examples=[24])


app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
template = Jinja2Templates(directory="templates")
users: list[User] = []


@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request) -> HTMLResponse:
    return template.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/admin")
async def user_admin() -> str:
    return "Вы вошли как администратор"


def get_user_from_id(user_id) -> User:
    for user in users:
        if user.id == user_id:
            return user


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_user(request: Request,
                   user_id: Annotated[int, Path(ge=1, le=100, description="Enter user ID", example=1)]) -> HTMLResponse:
    return template.TemplateResponse("users.html", {"request": request, "user": get_user_from_id(user_id)})


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


@app.post("/", response_class=HTMLResponse)
async def add_new_user(request: Request,
                       username: str = Form(min_length=5, max_length=20, description="Enter username",
                                            examples=["UrbanUser"]),
                       age: int = Form(ge=18, le=120, description="Enter age", examples=[24])) -> HTMLResponse:
    user_id = int(max((u.id for u in users), default=0) + 1)
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return template.TemplateResponse("users.html", {"request": request, "users": users})


@app.post("/user/{username}/{age}", response_model=User)
async def add_user(user: CreateUser) -> User:
    user_id = int(max((u.id for u in users), default=0) + 1)
    new_user = User(id=user_id, username=user.username, age=user.age)
    users.append(new_user)
    return new_user
