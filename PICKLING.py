import pickle

data = {"name": "Alice", "age": 25}

# Serializing 
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)

# Deserializing 
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)

print(loaded_data)  # Output: {'name': 'Alice', 'age': 25}
