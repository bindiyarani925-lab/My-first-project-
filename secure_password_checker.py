password = input("Enter your password: ")

length = len(password) >= 8
upper = any(ch.isupper() for ch in password)
lower = any(ch.islower() for ch in password)
digit = any(ch.isdigit() for ch in password)
special = any(not ch.isalnum() for ch in password)

score = length + upper + lower + digit + special

if score == 5:
    print("Strong Password")
elif score >= 3:
    print("Medium Password")
else:
    print("Weak Password")