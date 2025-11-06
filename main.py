from fastapi import FastAPI, HTTPException, Header
import jwt
from .auth import login_user, validate_user

app = FastAPI(title="Simple JWT Authentication API")


@app.get("/")
async def home():
    return {"message": "JWT Authentication API"}


@app.post("/login")
async def login(username: str, password: str):
    result = login_user(username, password)
    if "error" in result:
        raise HTTPException(status_code=401, detail=result["error"])
    return result

@app.post("/validate")
async def validate(token: str):
    result = validate_user(token)
    if "error" in result:
        raise HTTPException(status_code=401, detail=result["error"])
    return result

