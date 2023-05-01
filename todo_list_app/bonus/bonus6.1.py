contetnts = ["All carrots are to be sliced longuitudinally",
            "The carrots were reportedly sliced",
            "The slicing process was well presented"]
filenames=["doc.txt", "report.txt", "presentation.txt"]
for contetnt , filename in zip(contetnts, filenames):
    file= open(f"../files/{filename}", "w")
    file.write(contetnt)
