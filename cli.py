# Standard Library
import time

# Custom module import
# from functions import get_todos, write_todos # Import functions in the same level main.py
# import functions -> to call functions.get_todos() -> Import MODULE
from modules import functions as m

now = time.strftime("%b %d, %Y, %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith('add') or user_action.startswith('new') or user_action.startswith('more'):
        todo = user_action[4:]
        todos = m.get_todos()
        todos.append(todo + "\n")
        m.write_todos(filepath='files/todos/todos.txt', todos_arg=todos)

    elif user_action.startswith('show') or user_action.startswith('display') or user_action.startswith('pending'):
        todos = m.get_todos()
        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos):
            row = f"{index + 1}. {item}"  # interpolation data
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = user_action[5:]
            number = int(number) - 1
            todos = m.get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            m.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue  # instead break on match

    elif user_action.startswith('complete'):
        try:
            number = user_action[9:]
            todos = m.get_todos()
            index = int(number) - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            m.write_todos(todos)
            message = f"Your task '{todo_to_remove}' was removed from list. You got it!"
            print(message)

        except IndexError:
            print("There is not item with that number.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Hey!, you entered an unknown command")

print("Bye bye!")
