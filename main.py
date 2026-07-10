import random
import string

print("🔒🔒🔒🔒🔒🔒🔒🔒🔒")
print("ENTERPRISE PASSWORD GENERATOR")

length = int(input("Please enter the password length: "))

if length < 8:
    print("Password must be at least 8 characters.")
else:
    characters = string.punctuation + string.ascii_letters + string.digits
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("🔓🔓🔓🔓🔓🔓🔓🔓🔓")
    print("Generated Password:")
    print(password)