import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_punctuation=True):
    if length < 8:
        print("Password length must be at least 8 characters.")
        return None

    all_characters = string.ascii_lowercase
    if use_uppercase:
        all_characters += string.ascii_uppercase
    if use_numbers:
        all_characters += string.digits
    if use_punctuation:
        all_characters += string.punctuation

    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

length = int(input("Enter the length of the password (at least 8): "))

use_uppercase = input("Use uppercase letters? (y/n): ").lower() == 'y'
use_numbers = input("Use numbers? (y/n): ").lower() == 'y'
use_punctuation = input("Use punctuation? (y/n): ").lower() == 'y'

print("Generated Password : ", generate_password(length, use_uppercase, use_numbers, use_punctuation))