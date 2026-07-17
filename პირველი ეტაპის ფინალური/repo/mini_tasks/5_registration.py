"""
Registration Simulator
- Pre‑filled: email, username, password
- User enters only name
- Validate: must be lowercase Latin letters only
- Display all details on success
"""

import re

# Pre‑filled data
user_data = {
    "email": "user@mail.com",
    "username": "george777",
    "password": "password123"
}

def validate_name(name):
    # Must be only lowercase Latin letters
    if not name.isalpha():
        # check if it contains digits
        if any(c.isdigit() for c in name):
            return "შემოყვანილია რიცხვითი მნიშვნელობა, შემოიტანეთ მხოლოდ string პატარა რეგისტრში"
        elif any(not c.isascii() for c in name):
            return "შემოყვანილია სხვა ენის სიმბოლოები, შემოიტანეთ მხოლოდ ლათინური ასოები"
        else:
            return "შემოყვანილია სიმბოლოები, შემოიტანეთ მხოლოდ string პატარა რეგისტრში"
    elif not name.islower():
        return "შემოყვანილია დიდი ასოები, შემოიტანეთ მხოლოდ პატარა რეგისტრში"
    else:
        return None  # valid

def main():
    print("\n===== Registration Simulator =====")
    print("Please enter your name (only lowercase Latin letters):")
    name = input().strip()
    error = validate_name(name)
    if error:
        print(f"Error: {error}")
    else:
        # All good, register
        user_data["name"] = name
        print("\nRegistration successful!")
        print("Your details:")
        print(f"Email: {user_data['email']}")
        print(f"Name: {user_data['name']}")
        print(f"Username: {user_data['username']}")
        print(f"Password: {user_data['password']}")

if __name__ == "__main__":
    main()