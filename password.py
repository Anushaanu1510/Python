import random
import string


def generate_password(length):
    character = string.ascii_letters+ string.digits+ string.punctuation
    password=""
    for i in range(length):
        password+=random.choice(character)
    return password

length=int(input("Enter the length of the password:"))
print("The generated password is",generate_password(length))