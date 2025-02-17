import jwt
import datetime

SECRET_KEY = "your_secret_key"

# Simulated user database (Replace with a real database in production)
users_db = {
    "student1": "password123",
    "student2": "password456",
    "teacher1": "admin789"
}

def generate_jwt(user_id):
    """Generate JWT token for a user"""
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expires in 1 hour
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def login(user_id, password):
    """Authenticate user and generate JWT token"""
    if user_id in users_db and users_db[user_id] == password:
        token = generate_jwt(user_id)
        return {"message": "Login successful!", "token": token}
    else:
        return {"error": "Invalid credentials!"}

# Example usage
user1 = login("student1", "password123")
user2 = login("student2", "password456")

print(user1)  # JWT token for student1
print(user2)  # JWT token for student2
