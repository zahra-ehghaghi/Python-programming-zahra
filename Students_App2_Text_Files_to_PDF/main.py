from fpdf import FPDF
from glob import  glob
from pathlib import  Path
pdf= FPDF(orientation="p",unit="mm",format="A4")
filepaths=glob("textfiles/*.txt")
for file in filepaths:
    title =Path(file).stem
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=title.capitalize(),border=0,ln=1)
    with open(file,"r") as filedata:
        pdf.set_font(family="Times", style="", size=12)
        pdf.multi_cell(w=0, h=6, txt=str(filedata.read()), border=0)
pdf.output("output.pdf")









