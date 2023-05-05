from bonus.converter14 import convert

feet_inches = input("Please enter feet and inches: ")
from parser14 import parse

parsed= parse(feet_inches)
result = convert(parsed["feet"], parsed["inches"])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} metters")
if result < 1:
    print(f" Hi kid. you are {result} meter and you can not use slide")
else:
    print(f" Hi kid. you are {result} meter and you can use slide")
