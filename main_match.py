while True:
    # Get user inputs and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            # traditional way to open files
            # file = open('files/todos/todos.txt', 'r')
            # todos = file.readlines() # return a list []
            # file.close() # close memory reader

            # with context manager - recommended way instead traditional way
            with open('files/todos/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            # store data into text file
            with open('files/todos/todos.txt', 'w') as file_writer:
                file_writer.writelines(todos)

        case "edit":
            number = int(
                input("Enter a number of the TODO to edit: "))  # all inputs are string, needs be parsed with int
            number = number - 1

            with open('files/todos/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('files/todos/todos.txt', 'w') as file_writer:
                file_writer.writelines(todos)

        case "complete":
            number = int(input("Enter a number to complete: "))
            with open('files/todos/todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('files/todos/todos.txt', 'w') as file_writer:
                file_writer.writelines(todos)

            message = f"Your task '{todo_to_remove}' was removed from list. You got it!"
            print(message)
        case "show" | "display":
            with open('files/todos/todos.txt', 'r') as file:
                todos = file.readlines()

            # remove \n 1st way - for loop
            # new_todos = []
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            # remove \n 2nd way - for loop inline
            new_todos = [item.strip('\n') for item in todos]

            # print todos
            for index, item in enumerate(new_todos):
                # item = item.strip('\n') # simple solution remove \n
                row = f"{index + 1}. {item}"  # interpolation data
                print(row)
        # print("hello", index, item) if its out, print the last item
        case "exit":
            break
        case _:
            print("Hey!, you entered an unknown command")

print("Bye bye!")
