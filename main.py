# Custom Function
def get_todos():
    with open('files/todos/todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith('add') or user_action.startswith('new') or user_action.startswith('more'):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + "\n")
        with open('files/todos/todos.txt', 'w') as file_writer:
            file_writer.writelines(todos)

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
            with open('files/todos/todos.txt', 'w') as file_writer:
                file_writer.writelines(todos)

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
            with open('files/todos/todos.txt', 'w') as file_writer:
                file_writer.writelines(todos)
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
