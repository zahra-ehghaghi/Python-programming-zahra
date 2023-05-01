
def exercise_1():
    dolloar_str = input("Homany dollars have you got: ")
    if dolloar_str.isdecimal():
        dolloar_value=float()
        euros_value= dolloar_value * 0.95
        print (f"The amount in euros is : \n{euros_value}")
    else:
        print("Error, You Must Enter a number ")


def exercise_2():
    ranking = ['John', 'Sen', 'Lisa']
    rank_str = input("Enter rank number: ")
    if rank_str.isdigit():
        if int(rank_str) > ranking.__len__() or int(rank_str) <= 0:
            print(f"Error, You Must Enter a int value between 1 and {ranking.__len__()} ")
        else:
            print(ranking[int(rank_str)-1])
    else:
        print("Error, You Must Enter a int value ")

def exercise_3():
    ranking = ['John', 'Sen', 'Lisa']
    name = input("Enter a Name: ").strip()
    if ranking.__contains__(name):
        print(ranking.index(name)+1)
    else:
        print("Error, Your name is not in the list ")

#exercise_1()
#exercise_2()
exercise_3()

