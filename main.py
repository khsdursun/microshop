from typing import Annotated
from fastapi import FastAPI, Path
import uvicorn
from pydantic import BaseModel, EmailStr

app = FastAPI()

class CreateUser(BaseModel):
    email: EmailStr

@app.get("/")
async def root():
    return {
        "message": "Hello World"
    }

@app.get("/hello/")
async def hello_user(name: str = "World"):
    return {
        "message": f"Hello {name}!"
    }


@app.get("/items/")
async def read_item():
    return [
        "item_1",
        "item_2",
        "item_3",
    ]

@app.post("/users/")
async def create_user(user: CreateUser):
    return {
        "user": "success",
        "email": user.email,
    }

@app.get("/items/{item_id}/")
async def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "item": {
            "item_id": item_id,
    }
}

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)