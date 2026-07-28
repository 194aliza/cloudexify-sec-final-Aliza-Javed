import bcrypt
import json
import os

FILE_NAME = "users.json"

# Load Users
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        users = json.load(file)
else:
    users = {}



def login():
    print("\n===== Login =====")

    username = input("Username: ")
    password = input("Password: ")

    if username not in users:
        print("\nInvalid Username!")
        return

    stored_hash = users[username].encode()

    if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
        print("\nLogin Successful!")
    else:
        print("\nInvalid Password!")




print("\n===== Secure Authentication System =====")
print("1. Register")
print("2. Login")

choice = input("\nEnter your choice (1/2): ")



if choice == "1":

    print("\n===== Registration =====")

    username = input("Enter Username: ")

    if username in users:
        print("\nUser already exists! Please Login.")

        login()

    else:

        password = input("Enter Password: ")

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode()

        users[username] = hashed_password

        with open(FILE_NAME, "w") as file:
            json.dump(users, file, indent=4)

        print("\nRegistration Successful!")

        print("\nNow Login to continue.")

        login()



elif choice == "2":

    login()


else:

    print("\nInvalid Choice!") 
