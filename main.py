todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
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
        case "show" | "display":
            for item in todos:
                item = item.title()
                print(item)
        case "exit":
            break
        case _:
            print("Hey!, you entered an unknown command")

print("Bye bye!")