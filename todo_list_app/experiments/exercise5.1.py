def Exercise_1():
    filenames = ['document', 'report', 'presentation']
    for index,item in enumerate(filenames):
        print (f"{index}-{item}")

def Exercise_2():
    ips = ['100.122.133.105', '100.122.133.111']
    index = int(input("Enter the index of the IP you want: "))
    if(index >= len(ips)  or index <0):
        print("Selected index does not exist!!!")
    else:
        print(f"You choose {ips[index]}")
Exercise_2()