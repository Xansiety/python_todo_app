try:
    width = float(input("Enter rectangle width: "))
    height = float(input("Enter rectangle height: "))

    if width <= 0 or height <= 0:
        raise ValueError

    if width == height:
        exit("That looks like a square to me.")

    area = width * height
    print(f"The area of the rectangle is {area}")

except ValueError:
    print("Invalid input. Please enter a valid number.")
