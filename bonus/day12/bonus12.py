feet_inches = input("Enter feet and inches: ")


def convert(feet_inches_arg):
    parts = feet_inches_arg.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.304 + inches * 0.0254
    print_convertion(feet, inches, meters)
    return meters

def print_convertion(feet, inches, meters):
    print(f"{feet} feet and {inches} inches is equal to {meters} meters")

result = convert(feet_inches)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use slid.")



# Liters Converter Function
# Your task for this exercise is to:
#
# (1) define a function named liters_to_m3
#
# (2) the function should take a liters parameter
#
# (3) in the function you should converts liters to cubic meters (1000 liters = 1 cubic meters)
#
# (4) then, return the cubic meters.
#
# Note: Defining the function is enough. You do not need to call or print out a function output, but you should name the function exactly liters_to_m3.

def liters_to_m3(liters_arg):
    return liters_arg / 1000

liters = 1000
m3 = liters_to_m3(liters)
print(f"{liters} liters is equal to {m3} cubic meters")




# Password Validation Function
# Complete the strength function. The function will check the strength of a given password. Specifically, the function should:
#
# (1) get a password argument
#
# (2) return the string "Strong Password" if all of the following conditions are true:
#
# Password is 8 or more characters
#
# Password has at least one uppercase letter
#
# Password has at least one digit.
#
# (3) if one or more of the above conditions are not met, the function should return "Weak Password".

# Note:  You can make use of the code we developed in the Bonus Example on Day 9.

def strength(password_arg):
    if len(password_arg) >= 8 and any(i.isdigit() for i in password_arg) and any(i.isupper() for i in password_arg):
        return "Strong Password"
    else:
        return "Weak Password"

password = input("Enter your password: ")
print(strength(password))




# Average Function
# Define a function that:
#
# (1) takes a list as an argument
#
# (2) returns the average value of the list items.
#
# For example, if I called your function with foo([10, 20, 30, 40]) it should return 25 which is the average of the numbers of the list.
#
# Note: You can name the function anyway you want. It's enough to define the function. There is no need to call it.

def get_average(list_arg):
    return sum(list_arg) / len(list_arg)

numbers = [10, 20, 30, 40]
average = get_average(numbers)
print(average)