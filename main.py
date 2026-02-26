from fastapi import FastAPI
from models import User

app = FastAPI()

# Создаем экземпляр класса User
user = User(name="John Doe", id=1)

@app.get("/")
async def root():
    return {"message": "Добро пожаловать в API пользователей"}

@app.get("/users")
async def get_user():
    """
    GET-эндпоинт для получения информации о пользователе.
    Возвращает JSON с данными пользователя.
    """
    return {
        "user": user,
        "status": "success",
        "message": "Данные пользователя успешно получены"
    }


#uvicorn main:app --reload
#http://127.0.0.1:8000

#models.py: Содержит Pydantic модель User с обязательными полями name (строка) и id (целое число).

# main.py:

# Импортирует модель User из models.py

# Создает экземпляр класса User с указанными значениями

# Реализует GET-эндпоинт /users, который возвращает JSON с данными пользователя

# FastAPI автоматически сериализует объект User в JSON благодаря встроенной поддержке Pydantic моделей.

#curl.exe -X POST "http://127.0.0.1:8000/calculate" -H "Content-Type: application/json" -d '{\"num1\":5,\"num2\":10}'