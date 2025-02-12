todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())
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
            for index, item in enumerate(todos):
                row = f"{index + 1}. {item}" # interpolation data
                print(row)
        case "exit":
            break
        case _:
            print("Hey!, you entered an unknown command")

print("Bye bye!")