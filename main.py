from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

class LoginBody(BaseModel):
    email: str
    password: str

app = FastAPI()

#return index.html page on browser request
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def index():
    return FileResponse("static/index.html")

#get response on postman request
@app.get("/add/{no1}/{no2}")
def add(no1 : int , no2 : int):
   
    return {"total": no1 + no2}

@app.post("/login")
def login(loginBody: LoginBody):
    print(loginBody)
    return {"message": "Login successful"}