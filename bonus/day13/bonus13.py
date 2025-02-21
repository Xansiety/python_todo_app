# Decoupling's Principle
feet_inches = input("Enter feet and inches: ")


def parse(feet_inches_arg):
    parts = feet_inches_arg.split(" ")
    feet_float = float(parts[0])
    inches_float = float(parts[1])
    return feet_float, inches_float


def convert(feet_arg, inches_arg):
    meters = feet_arg * 0.304 + inches_arg * 0.0254
    return meters


feet, inches = parse(feet_inches)
result = convert(feet, inches)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use slid.")

# Age Function
# Define a function named get_age  which:
# (1) has two parameters, year_of_birth and current_year
# (2) the current_year  parameter should be a default parameter
# (3) the default value of current_year should be the current year (e.g., the integer 2025)
# (4) the function should calculate and return the age of the user given the year_of_birth and the current_year.


def get_age(year_of_birth, current_year=2025):
    age = current_year - year_of_birth
    return age

age = get_age(2000)
print(age)



# Write a get_nr_items function that:
# (1) gets as a parameter one string with commas (e.g., "john,lisa, teresa")
# (2) the function calculates the number of words (i.e., three words in the above example)
# (3) returns the number of words.
# For example, if I called your function with get_nr_items("john,lisa, teresa") it would return 3.

def get_nr_items(string_arg):
    nr_items = len(string_arg.split(","))
    return nr_items

nr_items = get_nr_items("john,lisa, teresa")
print(nr_items)


# Square Area Function
# Define a function that:
# (1) takes the side length of a square as a parameter
# (2) calculates and returns the area of a square.
# For example, if I was to call your function with foo(7)it would return 49.  You can name the function anyway you want.

def square_area(side_length_arg):
    area = side_length_arg * side_length_arg
    return area

area = square_area(7)
print(area)


# Temperature Checker
# Define a function that:
# (1) takes a temperature as a parameter
# (2) returns "Warm" if the temperature is greater than 7
# (3) returns "Cold" if the temperature is equal to or less than 7.
# If I called your function with foo(10) it would return Warm. If I called it with foo(7) or foo(5) it would return Cold and so on.

def temperature_checker(temperature_arg):
    if temperature_arg > 7:
        return "Warm"
    else:
        return "Cold"

temperature = temperature_checker(10)
print(temperature)


# Password Length Checker
# Define a function that:
# (1) takes a string as a parameter
# (2) returns False if the string contains less than 8 characters
# (3) returns True if the string contains 8 or more characters
# In other words, if I called your function with foo("mypass") it would return False. If I called it with foo("mylongpassword") it would return True, and so on.

def password_length_checker(password_arg):
    if len(password_arg) >= 8:
        return True
    else:
        return False

password = password_length_checker("mypass")
print(password)


# The following formula calculates the free-fall time of an object.

# t = sqrt(2 * h / g)

# Define a function that:
# h is the free-fall distance and g is the gravity. On Earth, gravity is 9.80665 m/s2.
# Given the above information, we have created a program that calculates
# the free-fall time given the free-fall distance h and the gravity g which will be a default parameter with a value of 9.80665:

def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)