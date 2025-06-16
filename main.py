from fastapi import FastAPI
from pydantic import BaseModel

class LoginBody(BaseModel):
    email: str
    password: str

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/add/{no1}/{no2}")
def add(no1 : int , no2 : int):
   
    return {"total": no1 + no2}

@app.post("/login")
def login(loginBody: LoginBody):
    print(loginBody)
    return {"message": "Login successful"}