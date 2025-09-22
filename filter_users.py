import json

def load_users(file_path = "users.json"):
    """Load users from JSON file"""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def filter_by_age(users):
    """Filter users by age"""
    filtered_users = []
    for user in users:
        age = user["age"]
        print(f"Name: {user['name']}, Age: {age}")

def filter_by_email(users):
    """Filter users by email"""
    filtered_users = []
    for user in users:
        email = user["email"]
        print(f"Name: {user['name']}, Email: {email}")

if __name__ == "__main__":
    users = load_users()
    filter_by_age(users)
    filter_by_email(users)