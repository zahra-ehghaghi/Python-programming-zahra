def exercise_1(liters_arg):
    try:
        cubic = float(liters_arg) / 1000
        return cubic
    except ValueError:
        return 0


def exercise_2(password_arg):
    isvalid = {"islength":False,"isdigit":False,"isupper":False}

    islength = len(password_arg) > 8
    isvalid["islength"] = islength
    for i in password_arg:
        if i.isdigit():
            isvalid["isdigit"] = True
    for i in password_arg:
        if i.isupper():
            isvalid["isupper"] = True
    return all(isvalid.values())




"""
call  exercise_1
"""
# liters = input("Enter liters value: ")
# cubic_val= exercise_1(liters)
# print(f"cubic value is equal to:{cubic_val}")


"""
call  exercise_2
"""
password = input("Enter password : ")
if exercise_2(password):
    print("Valid Password")
else:
    print("Weak password")