import jwt
import datetime
secret_key="secret_key"
payload= {
    "userid":10,
    "username":"coder"
}
token=jwt.encode(payload,secret_key,algorithm='HS256')
print(token)
