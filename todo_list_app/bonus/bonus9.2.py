password = input("Enter new password: ")
result= {}
if len(password) <= 8:
    result["length"] = False
else:
    result["length"] = True
digits= False
for i in password:
    if i.isdigit():
        digits = True
result["digits"]= digits
upser_case = False
for i in password:
    if i.isupper():
        upser_case = True
result["upser_case"]= upser_case

print(result)
if(all(result.values())):
    print("Strong Password")
else:
    print("Weak Password")




