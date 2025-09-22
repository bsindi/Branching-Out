from filter_users import load_users, filter_by_age, filter_by_email

if __name__ == "__main__":
    # Load all users from the JSON file
    users = load_users()

    # Display all users with their age
    print("\nFilter by Age:")
    filter_by_age(users)

    # Display all users with their email
    print("\nFilter by Email:")
    filter_by_email(users)
