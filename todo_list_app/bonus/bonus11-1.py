def get_average():
    with open("files/data.txt", "r") as file:
        numbers= file.readlines()
    sum = 0
    print(numbers)
    for index, number in enumerate(numbers):
        try:
            sum += float(number)
        except ValueError:
            index -=1
            continue
    return sum/index


average = get_average()
print(average)
