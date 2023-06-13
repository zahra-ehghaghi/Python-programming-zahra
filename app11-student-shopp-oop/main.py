import  pandas as pd
from fpdf import  FPDF
df =pd.read_csv("articles.csv",dtype={"id":str})
class Article:
    def __init__(self,id):
        self.id = id
        self.name=df.loc[df["id"] == self.id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.id, "price"].squeeze()

    def buy(self):
       print(self.id)
       df.loc[df["id"] == self.id, "in stock"] =df.loc[df["id"] == self.id, "in stock"].squeeze() -1
       df.to_csv("articles.csv",index=False)
    def available(self):
        in_stock = df.loc[df["id"] == self.id, "in stock"].squeeze()
        if in_stock > 0:
             return  True
        else:
            return  False


class Receipt():
    def __init__(self,article):
        self.article = article

    def generation(self):
        pdf = FPDF(orientation="P", unit="mm" , format="a4")
        pdf.add_page()
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50,h=8,txt=f"Reciept Nr.{self.article.id}", ln=1)
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name}", ln=1)
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)
        pdf.output("Receipt.pdf")

print(df)
id = input("Enter a id for shopping: ")
article = Article(id)
if article.available():
    article.buy()
    receipt = Receipt(article)
    receipt.generation()
else:
    print("Sock is empty")
