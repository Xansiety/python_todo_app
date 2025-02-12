# Data in-mutability
filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentation.txt"]

for filename in filenames:
    filename = filename.replace('.', '-', 1) # only replace the first ocurrence
    print(filename)


# List can be inmutables using tuples - use () instead []
filename = ("1.Raw Data.txt", "2.Reports.txt", "3.Presentation.txt")

# filename
# ('1.Raw Data.txt', '2.Reports.txt', '3.Presentation.txt')
# type(filename)
# <class 'tuple'>
# filename[1]
# '2.Reports.txt'
# filename[1] = "something new"
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# filename.append()
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# AttributeError: 'tuple' object has no attribute 'append'
