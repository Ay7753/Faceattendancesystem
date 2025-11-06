import jwt


SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"


db = {
    "ayush": {"username": "ayush", "password": "12345", "email": "ayush@example.com"},
    "admin": {"username": "admin", "password": "admin123", "email": "admin@example.com"},
}


def authenticate_user(username: str, password: str):
    
    user = db.get(username)
    if not user or user["password"] != password:
        return None
    return user


def login_user(username: str, password: str):
    user = authenticate_user(username, password)
    if not user:
        return {"error": "Invalid username or password"}

    
    token = jwt.encode({"username": user["username"], "email": user["email"]}, SECRET_KEY, algorithm=ALGORITHM)
    return {"token": token}

def validate_user(token: str):
   
    decoded_user = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    return {
        "user_details": decoded_user
    }
                             
