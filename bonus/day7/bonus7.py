filenames = ["1.doc", "1.report", "1.presentation"]

# List Comprehension
filenames = [filename.replace(".", "-") + ".txt" for filename in filenames]

print(filenames)

# >>> ['1-doc.txt', '1-report.txt', '1-presentation.txt']

names = ["john smith", "jay santi", "eva kuki"]

names = [name.title() for name in names]
print(names)

usernames = ["john 1990", "alberta1970", "magnola2000"]
usernames = [len(username) for username in usernames]
print(usernames)

user_entries = ['10', '19.1', '20']
user_entries = [float(entry) for entry in user_entries]
print(user_entries)


numbers = [10, 20, 30]
numbers = [number * 2 for number in numbers]
print(numbers)


user_entries = ['10', '19.1', '20']
user_entries = [float(entry) for entry in user_entries]
print(sum(user_entries))