import bcrypt
name = input("Enter your name: ")
password = input("Enter your password: ")

password_bytes = password.encode("utf-8")

salt = bcrypt.gensalt()

hashed_password = bcrypt.hashpw(password_bytes, salt)

print("\nOriginal Password:", password)
print("Hashed Password:", hashed_password.decode())
