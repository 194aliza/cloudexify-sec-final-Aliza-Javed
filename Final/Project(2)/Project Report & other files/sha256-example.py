import hashlib 
name = input("Enter name: ")
password = input("Enter Password: ")

hashed = hashlib.sha256(password.encode("utf-8")).hexdigest()

print("\nSHA-256 Hash:")
print(hashed)
