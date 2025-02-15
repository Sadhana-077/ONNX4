import jwt
import datetime
secret_key="secret_key"
payload={
    "user_id":11,
    "username":"coder",
   
}

token=jwt.encode(payload,secret_key,algorithm="HS256")
print("username:coder || ",token)




