feet_inches = input("Please enter feet and inches: ")


def convert(feet_inches_arg):
    parts = feet_inches_arg.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    meters = feet * 0.3048 + inches * 0.0254
    return meters


result = convert(feet_inches)
if result < 1:
    print(f" Hi kid. you are {result} meter and you can not use slide")
else:
    print(f" Hi kid. you are {result} meter and you can use slide")
