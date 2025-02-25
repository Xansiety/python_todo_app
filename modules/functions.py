# Custom Function
FILEPATH = "files/todos/todos.txt"


def get_todos(filepath=FILEPATH):
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
def write_todos(todos_arg: list[str], filepath=FILEPATH):
    """ Write the to-do items list in the text file
     Args:
         todos_arg: list. The list of to-do items
         filepath: str. The path to the file to write
     Returns:
         None
    """
    with open(filepath, 'w') as file_writer:
        file_writer.writelines(todos_arg)


# When a file is imported, it is executed by default
# print("hello from functions.py")

# How can prevent this?
# Add if __name__ == '__main__': to execute the code only when the file is run directly not imported
# When the file is the value of __name__ variable: '__main__', only when the file is run directly
if __name__ == '__main__':
    print("hello from functions.py")
    print(get_todos())
