# Custom Function
def get_todos(filepath="files/todos/todos.txt"):
    """ Read a text file and return the list of to-do items
     Args:
         filepath: str. The path to the file to read
     Returns:
         list. The list of to-do items
     """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# Can't put an optional argument after the default arg
def write_todos(todos_arg: list[str], filepath="files/todos/todos.txt"):
    """ Write the to-do items list in the text file
     Args:
         todos_arg: list. The list of to-do items
         filepath: str. The path to the file to write
     Returns:
         None
    """
    with open(filepath, 'w') as file_writer:
        file_writer.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith('add') or user_action.startswith('new') or user_action.startswith('more'):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + "\n")
        write_todos(filepath='files/todos/todos.txt', todos_arg=todos)

    elif user_action.startswith('show') or user_action.startswith('display') or user_action.startswith('pending'):
        todos = get_todos()
        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos):
            row = f"{index + 1}. {item}"  # interpolation data
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = user_action[5:]
            number = int(number) - 1
            todos = get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue  # instead break on match

    elif user_action.startswith('complete'):
        try:
            number = user_action[9:]
            todos = get_todos()
            index = int(number) - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            write_todos(todos)
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
