password = input("Enter new password: ")
result=True
if len(password) <= 8 :
    result= False
if result:
    for index, item in enumerate(password):
        if item.isdigit():
            break
    if index == len(password)-1:
        result = False
if result:
    for index, item in enumerate(password):
        if item.isupper():
            break
    if index == len(password)-1:
        result = False

if result :
    print("Strong Password")
else:
    print("Weak Password")





