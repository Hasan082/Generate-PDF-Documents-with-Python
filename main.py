from fpdf import FPDF
import pandas as pd

# create FPDF object
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Create a DataFrame
df = pd.read_csv("topics.csv")

# Iterate through each row of the DataFrame(csv file)
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.set_text_color(0, 100, 100)
    pdf.cell(w=0, h=15, txt=row["Topic"], ln=1, align="L")
    pdf.line(10, 22, 200, 22)


pdf.output("tuto1.pdf")
