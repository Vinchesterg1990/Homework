from http.client import HTTPException

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int = None
@app.get('/users')
async def get_users() -> list:
    return users

@app.post('/user/{username}/{age}')
async def add_user(user: User,
                   username: str = Path(min_length=5, max_length=20, description='Enter username', example='Ivan'),
                   age: int = Path(ge=18, le=120, description='Enter your age', example='16')) -> str:
    user.id = 1 if len(users) == 0 else len(users) + 1
    user.username = username
    user.age = age
    users.append(user)
    return f'User {user.id} is registered.'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int,
                      username: str = Path(min_length=5, max_length=20, description='Enter username',
                                           example='Ivan'),
                      age: int = Path(ge=18, le=120, description='Enter your age', example='34')) -> str:
    try:
        edit_user = next(user for user in users if user.id == user_id)
        edit_user.username = username
        edit_user.age = age
        return f'User {user_id} has been updated.'
    except Exception:
        raise HTTPException(status_code=404, detail='User not found')
@app.delete('/user/{user_id}')
async def delete (user_id: int):
    raise2 = True
    ind_del = 0
    for delete_user in users:
        if delete_user.id == user_id:
            users.pop(ind_del)
            return delete_user
        ind_del += 1
    if raise2:
        raise HTTPException(status_code=404, detail='User was not found')

# uvicorn module_16_4:app
