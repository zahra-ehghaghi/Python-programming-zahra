feet_inches = input("Please enter feet and inches: ")


def parse (feet_inches_arg):
    parts = feet_inches_arg.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return  {"feet":feet, "inches":inches}

def convert(feet ,inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters
parsed= parse(feet_inches)
result = convert(parsed["feet"],parsed["inches"])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} metters")
if result < 1:
    print(f" Hi kid. you are {result} meter and you can not use slide")
else:
    print(f" Hi kid. you are {result} meter and you can use slide")
