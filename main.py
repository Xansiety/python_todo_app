user_prompt = "Enter a TODO:"

todos = []

# While loop
while True:
    todo = input(user_prompt)
    todo.capitalize() # Capitalize first letter
    todos.append(todo)
    print(todos)
