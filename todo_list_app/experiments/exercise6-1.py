filenames=["doc.txt", "report.txt", "presentation.txt"]



"""
Please download the essay.txt file from the resources of this article. Then, create a program that reads
that file and prints out its text. The first letter of each word in the output should be uppercase.
"""
def Exercise_1():
    file = open("essay.txt","r")
    content = file.read()
    print(content.title())

"""
Write a program that reads the essay.txt file and returns the number of characters contained in the file.
"""
def Exercise_2():
    file = open("essay.txt","r")
    content = file.read()
    print(len(content))

"""
Please download the members.txt file from the resources of this article. 
Then, create a program that, whenever executed, asks the user to enter a new member in the command line: 
Then, the member is added to members.txt. In this case, the text file content would be:
"""

def Exercise_3():
    user_message = input("Enter a new member : ")
    file = open("members.txt",'a')
    file.write(user_message)

"""
Create a program that generates multiple text files by iterating over the filenames list.
 The text Hello should be written inside each generated text file.
"""
def Exercise_4():
    for filename in filenames:
        file = open(f"{filename}",'w')
        file.write("Hello")
        file.close()
def Exercise_5():
    filenames = ["a.txt", "b.txt", "c.txt"]
    for filename in filenames:
        file = open(f"{filename}",'r')
        print(file.read())
        file.close()


Exercise_5()

