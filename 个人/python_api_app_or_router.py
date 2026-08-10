# 有没有prefix的区别主要是结构化、和规整（swagger）

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI

class User(BaseModel):
  id: int
  name: str
  description: str

@app.get('/user/user_id')
async def get_user_name(user_id) -> User:
