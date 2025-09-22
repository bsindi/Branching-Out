import json

def load_users(file_path="users.json"):
    """Load users from a JSON file"""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def filter_by_age(users):
    """Print all users with their age"""
    for user in users:
        # Print each user's name and age
        print(f"Name: {user['name']}, Age: {user['age']}")


def filter_by_email(users):
    """Print all users with their email"""
    for user in users:
        # Print each user's name and email
        print(f"Name: {user['name']}, Email: {user['email']}")
