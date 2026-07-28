import bcrypt
name = input("Enter your name: ")
password = input("Create Password: ")

password_bytes = password.encode("utf-8")

hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

print ("\nPassword stored successfully!\n")
user_login = input("Enter name to login: ")
login_password = input("Enter Password to Login: ")
if user_login == name:
 if bcrypt.checkpw(login_password.encode("utf-8"), hashed_password):
    print ("\nLogin Successful!")
 else:
    print ("\nInvalid Password!")
else:
  print ("\nInvalid user! ") 
