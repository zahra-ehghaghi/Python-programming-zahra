import  csv
with open("../files/weather.csv", "r") as file:
    data = list(csv.reader(file))
city = input("Please enter a city: ")
for temp in data[1:]:
    if temp[0] == city:
        print(temp[1])
        exit(0)
exit("THe city not found")
