from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel
from typing import Annotated

app = FastAPI()
templates = Jinja2Templates(directory='templates')

users = []


class User(BaseModel):
    id: int  # номер пользователя(int)
    username: str  #имя пользователя(str)
    age: int  #возраст пользователя (int)


@app.get('/')
async def get_all_message(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get(path='/user/{user_id}')
async def get_message(request: Request, user_id: int) -> HTMLResponse:

    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    else:
        return templates.TemplateResponse('users.html', {'request': request, 'user': user})


@app.post(path='/user/{username}/{age}')
async def post_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> User:
    new_id = (users[-1].id + 1) if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put(path='/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user

        else:
            raise HTTPException(status_code=404, detail="User was not found")


@app.delete(path='/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')]) -> User:
    for i, user in enumerate(users):
        if user.id == user_id:
            return users.pop(i)

    else:
        raise HTTPException(status_code=404, detail='User was not found')