from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("Arial", size=15)
pdf.cell(w=0, h=15, txt="Hello World!", ln=1, align="L", border=1)
pdf.cell(w=0, h=15, txt="Hi there!", ln=1, align="L")
pdf.output("tuto1.pdf")
