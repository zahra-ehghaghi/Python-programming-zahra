head_number = 0
total_try = 0
while True:
    choise = input("Throw the coin and enter head or tail here: ")
    if choise == "head":
        head_number += 1
    total_try += 1
    percent = head_number / total_try * 100
    print("Heads:" + str(percent))