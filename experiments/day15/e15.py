import glob

myfiles = glob.glob("../../files/bonus/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())
