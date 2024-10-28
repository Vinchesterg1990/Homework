from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def start_page()-> dict:
    return {"Mesage": "Главная страница"}

@app.get("/user/admin")
async def welcom_admin()-> dict:
    return {"Mesage": "Вы вошли как администратор"}

@app.get('/user/{user_id}')
async def user(user_id):
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get('/user')
async def user_info(username, age):
    return f'Информация о пользователе, Имя: {username}, Возраст: {age}'

# uvicorn main:app