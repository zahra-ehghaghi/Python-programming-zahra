def Exercise_1():
    try:
        total = float(input("Enter total value:"))
        value = float(input("Enter value:"))
        percent = value / total
        print(f"That is : {percent}")
    except ValueError:
        print("please enter valid number, Run the program againt")
    except ZeroDivisionError:
        print("Your total value cannot be zero")
Exercise_1()


