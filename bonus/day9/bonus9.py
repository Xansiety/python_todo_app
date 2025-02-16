password = input("Enter new password: ")

result = {}  # to create a dictionary use {} instead brackets (brackets are for list)

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["upper-case"] = uppercase

# Dictionary

# print(result)
# print(result.keys(), result.values())
if all(result.values()):
    print("Strong Password")
else:
    print("Weak password")


# Tuples in python
day_temperatures = {'morning': (1.1, 2.2, 3.4), 'noon': (2.3, 4.5, 3.1), 'evening': (2.4, 3.5, 6.5)}