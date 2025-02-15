from fastapi import FastAPI
import jwt
app=FastAPI()
@app.get("/verify/{token}")
def verify_token(token:str):
    try:
        payload=jwt.decode(token,"secret_key",algorithms=['HS256'])
        print(payload)
        return payload
    except jwt.ExpiredSignatureError:
        print("token has expired")
    except jwt.InvalidTokenError:
        print("Invalid Token")    
    return {}    
@app.get("login/verify/{username}")
def login(username):
    secret_key="secret_key"
    if username!="coder":
        return {}
    payload = {
        "userid":10,
        "username":username,
    }    
token=jwt.encode(payload,secret_key,algorithm="HS256")
return token