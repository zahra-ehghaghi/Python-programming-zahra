def calculate_age(year_of_birth,current_year=1402):
    return current_year-year_of_birth

def calculate_number_of_items(names_arg):
    names_value= names_arg.split(" ")
    return len(names_value)


def calculate_time(h,g=9.80665):
    t = (2 * h / g) ** 0.5
    return t
# year = input("Enter your year of birth: ")
# print(calculate_age(int(year)))


# names_str =input("Enter a list of names: ")
# names = calculate_number_of_items(names_str)
# print(names)

time = calculate_time(100)
print(time)