from random import randint
def calculate_random(lower_bound_arg, upper_bound_arg):
    return randint(int(lower_bound_arg),int(upper_bound_arg))



lower_bound = input("Enter the lower bound: ")
upper_bound = input("Enter the upper bound: ")
print(calculate_random(lower_bound,upper_bound))