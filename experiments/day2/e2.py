user_prompt = "Enter a TODO:"
todos = []

# While loop
while True:
    todo = input(user_prompt)
    todo.capitalize() # Capitalize first letter
    print(todo.title()) # Capitalize every first letter from words
    todos.append(todo)
    print(todos)