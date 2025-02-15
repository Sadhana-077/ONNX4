import requests
username="coder"
response_item=requests.get(f"http://127.0.0.1:8000/login/{username}")
token=response_item.json()
print("token",response_item.json()) 
response_item=requests.get(f"http://127.0.0.1:8000/verify/{token}")
print('received from server:',response_item.json)