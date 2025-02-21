def get_average():
    with open('../files/data.txt', 'r') as file:
        data = file.readlines()
    values = data[1:]  # skip the first line
    numbers = [float(item.strip('\n')) for item in values]
    average_local = sum(numbers) / len(numbers)
    return average_local


average = get_average()
print(average)


def get_average():
    print("Hi")
    x = "hello"
    return x.capitalize()


get_average()

