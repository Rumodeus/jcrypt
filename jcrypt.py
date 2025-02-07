import random

def encrypt(string, pin):
    random.seed(str(pin))
    encrypted = [(ord(c) ^ random.randint(0, 255)) * int(pin) + 21008 for c in string]
    encrypted_data = ".".join(map(str, encrypted))
    return encrypted_data

def decrypt(string, pin):
    random.seed(str(pin))
    encrypted_numbers = list(map(int, string.split(".")))
    decrypted_chars = [chr((num - 21008) // int(pin) ^ random.randint(0, 255)) for num in encrypted_numbers]
    return "".join(decrypted_chars)

string = input("Enter text: ")
pin = input("Enter a PIN: ")
choice = input("Encrypt or Decrypt (e/d)? ")

if choice == "e":
    print(encrypt(string, pin))
    input("Press Enter to exit...")
elif choice == "d":
    print(decrypt(string, pin))
    input("Press Enter to exit...")
else:
    print("Invalid choice!")
