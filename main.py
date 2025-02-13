while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            file = open('files/todos/todos.txt', 'r')
            todos = file.readlines() # return a list []
            file.close() # close memory reader

            todos.append(todo)

            # store data into text file
            file_writer = open('files/todos/todos.txt', 'w')
            file_writer.writelines(todos)
            file_writer.close()

        case "edit":
            number = int(input("Enter a number of the TODO to edit: ")) # all inputs are string, needs be parsed with int
            number = number - 1
            # -- list indexing --
            existing_todo = todos[number]
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Enter a number to complete: "))
            todos.pop(number - 1)
        case "show" | "display":
            file = open('files/todos/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                row = f"{index + 1}. {item}" # interpolation data
                print(row)
        # print("hello", index, item) if its out, print the last item
        case "exit":
            break
        case _:
            print("Hey!, you entered an unknown command")

print("Bye bye!")