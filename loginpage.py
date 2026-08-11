import hashlib
import os

FILE_NAME = "users.txt"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register():
    print("\n===== REGISTRATION =====")

    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check whether username already exists
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                saved_username, saved_password = line.strip().split(":")
                if saved_username == username:
                    print("Username already exists!")
                    return

    password_hash = hash_password(password)

    with open(FILE_NAME, "a") as file:
        file.write(username + ":" + password_hash + "\n")

    print("Registration successful!")


def login():
    print("\n===== LOGIN =====")

    username = input("Enter username: ")
    password = input("Enter password: ")

    password_hash = hash_password(password)

    if not os.path.exists(FILE_NAME):
        print("No users registered yet.")
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            saved_username, saved_password = line.strip().split(":")

            if saved_username == username and saved_password == password_hash:
                print("Login successful!")
                print("Welcome,", username)
                return

    print("Invalid username or password!")


while True:
    print("\n===== SIMPLE LOGIN SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice!") 