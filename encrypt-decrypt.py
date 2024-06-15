# #!C:\msys64\mingw64\bin\python3.exe
import os
import random
import string

def generate_key():
    """Generate a random string of 26 characters"""
    return "".join(random.choice(string.ascii_lowercase) for _ in range(26))

def encrypt_decrypt(file, key, decrypt=False):
    """Encrypt or decrypt a file with a key"""
    if decrypt:
        mapping = str.maketrans(key, string.ascii_lowercase)
    else:
        mapping = str.maketrans(string.ascii_lowercase, key)

    with open(file, "r") as f:
        content = f.read()  

    new_content = content.translate(mapping)  

    with open(file, "w") as f:
        f.write(new_content)  

def change_extension(file, new_extension):
    """Change the extension of a file"""
    base, _ = os.path.splitext(file)  # Split the file into base and extension
    new_name = base + new_extension  # Concatenate the base with the new extension
    os.rename(file, new_name)  
    return new_name

def main():
    file = "test.txt"  # File 
    key = generate_key()  
    print(f"Key: {key}")  

    encrypt_decrypt(file, key)  # Encrypt the file
    print(f"{file} has been encrypted")  

    # Change the extension of the file
    new_name = change_extension(file, ".jiji")
    print(f"New name: {new_name}")

    input("Press enter to decrypt ;) ")

    original_file_name = change_extension(new_name, ".txt")

    # Decrypt the file
    encrypt_decrypt(original_file_name, key, decrypt=True)  
    print(f"{original_file_name} has been decrypted")  

if __name__ == "__main__":
    main()


