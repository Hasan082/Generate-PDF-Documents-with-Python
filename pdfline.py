from fpdf import FPDF
import pandas as pd

# create FPDF object
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

# Create a DataFrame
df = pd.read_csv("topics.csv")

# Iterate through each row of the DataFrame(csv file)
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.set_text_color(0, 100, 100)
    pdf.cell(w=0, h=15, txt=row["Topic"], ln=1, align="L")
    for y in range(20, 290, 10):
        pdf.line(10, y, 200, y)

    # Set the foot note
    pdf.ln(260)
    pdf.set_font("Arial", size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], ln=1, align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # Set the foot note
        for y in range(20, 290, 10):
            pdf.line(10, y, 200, y)
        pdf.set_font("Arial", size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], ln=1, align="R")



pdf.output("pdflines.pdf")
