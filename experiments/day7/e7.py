with open('../../files/bonus/doc.txt') as file: # by default read mode is 'r', so not needed to specify, but it's a good practice
    content = file.read()

# this line should throw an error, because needs to be part of the context, I mean inside the with block(indentation), otherwise it will throw an error due to file it's closed
#print(file.read())

print(content)
