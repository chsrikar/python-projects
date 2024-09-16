import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

password_length = int(input("Enter the desired length of the password: "))
print("Generated Password:", generate_password(password_length))