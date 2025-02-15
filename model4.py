from fastapi import FastAPI, Depends
import jwt
import datetime

SECRET_KEY = "your_secret_key"

app = FastAPI()

def create_jwt_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expiry
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

@app.post("/login")
def login(user_id: str):
    token = create_jwt_token(user_id)
    return {"access_token": token}
