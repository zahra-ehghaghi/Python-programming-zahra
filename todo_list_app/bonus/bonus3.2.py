prompt_message="enter you country from USA, India or Germany or exit for exit: "
while True:
    user_country=input(prompt_message)
    match user_country.strip():
        case 'exit':
            break
        case 'USA':
            print("Hello")
        case 'India':
            print("Namasta")
        case 'Germany':
            print ("Hallo")
        case _:
            print("Your data is not corretc. please try again")
print("Bye!!!")

