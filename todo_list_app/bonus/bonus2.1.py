password="zahra"
prompt_message = "Enter password "
print (prompt_message.__len__())
con  = True
while con:
    user_pass = input(prompt_message)
    if user_pass.__eq__(password):
        print ("Password was correct")
        con = False
    else:
        print ("Password was not correct")


