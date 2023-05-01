date = input("Enter today's date: " )
mode = input("How do you rate your mood today from 1 to 8: ")
thoughts= input("Let your thoughts flow: ")
with open(f"../journal/{date}","w") as file:
    file.write(mode + 2 * "\n")
    file.write(thoughts)
