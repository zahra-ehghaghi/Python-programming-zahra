def Exercise_1():
    password = input("Enter a new password: ")
    if len(password) > 7:
        print("Greate password there!!")
    elif len(password) == 7 :
        print("Password is OK, but not too strong")
    else:
        print("Your Password is Weak")


Exercise_1()

