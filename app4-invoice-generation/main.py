import pandas
from fpdf import  FPDF
import  glob
from datetime import date
from pathlib import Path
filepaths = glob.glob("invoices/*.xlsx")
for file in filepaths:

    total = 0
    pdf = FPDF(orientation="L",unit="mm",format="A4")
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=16)
    invoice_nr, date = Path(file).stem.split('-')
    pdf.cell(w=50, h=8, txt=f"InvoiceNo:{invoice_nr}", align="L", border=0,ln=1)
    pdf.cell(w=50, h=8, txt=f"Date: {date}", align="L", border=0,ln=1)

    df = pandas.read_excel(file)
    pdf.set_font(family="Times", style="B", size=10)
    for title in df.keys():
        pdf.cell(w=55, h=12, txt=str(title).title().replace("_"," "), align="L", border=1)

    pdf.ln(12)
    height = 12
    pdf.set_font(family="Times", style="", size=12)
    for index, row in df.iterrows():
        for title in df.keys():
            txt = row[title]
            pdf.cell(w=55, h=12, txt=str(row[title]), align="L", border=1)
        pdf.ln(height)
    for title in df.keys():
        if title =="total_price":
            pdf.cell(w=55, h=12, txt=str(df['total_price'].sum()), align="L", border=1)
        else:
            pdf.cell(w=55, h=12, txt="", align="L", border=1)

    pdf.ln(height+5)
    pdf.set_font(family="Times", style="B", size=15)
    pdf.cell(w=0, h=12, txt=f"The total due amount is {df['total_price'].sum()} Euros", align="L", border=0)
    pdf.ln(height )
    pdf.cell(w=30, h=12, txt="PythonHow", align="L", border=0)
    pdf.image("pythonhow.png",w=10)
    pdf.output(f"pdfs/{Path(file).stem}.pdf")