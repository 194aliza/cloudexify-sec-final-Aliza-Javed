from cryptography.fernet import Fernet, InvalidToken

while True:

    message = input("\nEnter a message (-1 to Exit): ")

    if message == "-1":
        print("\nProgram Terminated.")
        break

    # Generate Secret Key
    key = Fernet.generate_key()
    cipher = Fernet(key)

    # Encrypt Message
    encrypted = cipher.encrypt(message.encode())

    print("\n===== Encryption Complete =====")
    print("Secret Key:")
    print(key.decode())

    print("\nEncrypted Message:")
    print(encrypted.decode())

    # Ask for Secret Key
    entered_key = input("\nEnter Secret Key to Decrypt: ")

    try:
        cipher2 = Fernet(entered_key.encode())
        decrypted = cipher2.decrypt(encrypted)

        print("\nDecrypted Message:")
        print(decrypted.decode())

    except InvalidToken:
        print("\nError: Wrong Secret Key! Decryption Failed.")

    except Exception:
        print("\nInvalid Key Format!")
