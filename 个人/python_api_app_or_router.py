# 有没有prefix的区别主要是结构化、和规整（swagger），app写法是：

from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

DB_PATH = "./backend/user.db"

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    description: str

@app.get('/user/{user_id}')
async def get_user_name(user_id: int) -> User:
    async with db_pool.connect as conn:
        row = await conn.fetch("SELECT id FROM WHERE GROUPBY")
    user_name = row.name
    return User(id = user_id, name = user_name, description = "developer")

# router写法是：

from fastapi import FastAPI
from pydantic import 
