filenames=["1.doc","1.report","1.presentation"]
new_filenames=[item.replace(".","-")+".txt" for item in filenames]
print(new_filenames)