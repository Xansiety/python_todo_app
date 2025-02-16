while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    if 'add' in user_action or 'new' in user_action or 'more' in user_action:
        todo = user_action[4:]
        with open('files/todos/todos.txt', 'r') as file:
            todos = file.readlines()
        todos.append(todo + "\n")
        with open('files/todos/todos.txt', 'w') as file_writer:
            file_writer.writelines(todos)

    elif 'show' in user_action or 'display' in user_action or 'pending' in user_action:
        with open('files/todos/todos.txt', 'r') as file:
            todos = file.readlines()
        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos):
            row = f"{index + 1}. {item}"  # interpolation data
            print(row)

    elif 'edit' in user_action:
        number = user_action[5:]
        number = int(number) - 1
        with open('files/todos/todos.txt', 'r') as file:
            todos = file.readlines()
        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'
        with open('files/todos/todos.txt', 'w') as file_writer:
            file_writer.writelines(todos)

    elif 'complete' in user_action:
        number = user_action[9:]
        with open('files/todos/todos.txt', 'r') as file:
            todos = file.readlines()
        index = int(number) - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)
        with open('files/todos/todos.txt', 'w') as file_writer:
            file_writer.writelines(todos)
        message = f"Your task '{todo_to_remove}' was removed from list. You got it!"
        print(message)

    elif 'exit' in user_action:
        break

    else:
        print("Hey!, you entered an unknown command")

print("Bye bye!")
