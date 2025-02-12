from operator import truediv

waiting_list = ["sen", "ben", "john"]
waiting_list.sort() # order by name reverse by default is false

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)