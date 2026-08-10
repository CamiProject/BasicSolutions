# 有没有prefix的区别主要是结构化、和规整（swagger），app写法是：

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI

class User(BaseModel):
    id: int
    name: str
    description: str

@app.get('/user/user_id')
async def get_user_name(user_id) -> User:
    user_name = await db.get()
    return User(id = user_id, name = user_name, description = "developer")

# router写法是：

from fastapi import FastAPI
from pydantic import 
