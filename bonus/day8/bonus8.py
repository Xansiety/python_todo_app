date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10: ")
thoughts = input("Let your thoughts flow:\n")

with open(f"../../journal/{date}.txt", "w") as file:
    file.write(f"Date: {date}\nMood: {mood}\n\n{thoughts}")

print("Your journal entry has been saved.")