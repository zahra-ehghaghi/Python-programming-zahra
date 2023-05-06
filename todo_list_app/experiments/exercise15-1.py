import glob
files = glob.glob("../files/*.txt")

for filepath in files:
    with open(filepath,"r") as file:
        print(file.read())
