# Decoupling's Principle
from bonus.day14.parsers14 import parse
from bonus.day14.utils14 import print_convertion
from bonus.day14.converters14 import convert

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)
feet = parsed["feet"]
inches = parsed["inches"]

result = convert(feet, inches)
print_convertion(feet, inches, result)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use slid.")
