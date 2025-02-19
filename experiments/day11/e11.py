def greet():
    message = "Hello"
    new_message = message.capitalize()
    print("Hey, Hey")
    return new_message

greeting = greet()
print(greeting)
print(greet())


# By default, None is returned if there is no return, or no return statement exists
def greet_none():
    print("None is returned if there is no return, or no return statement exists")

print(greet_none())