from reportlab.pdfgen import canvas


output_file = "data/pdfs/business_report.pdf"


pdf = canvas.Canvas(output_file)

pdf.setTitle("Business Performance Report")

pdf.drawString(50, 800, "Business Performance Report")
pdf.drawString(50, 770, "Employee: Amit")
pdf.drawString(50, 750, "Department: IT")
pdf.drawString(50, 730, "Tasks Assigned: 20")
pdf.drawString(50, 710, "Tasks Completed: 18")
pdf.drawString(50, 690, "Completion Percentage: 90%")

pdf.drawString(50, 650, "Employee: Neha")
pdf.drawString(50, 630, "Department: HR")
pdf.drawString(50, 610, "Tasks Assigned: 15")
pdf.drawString(50, 590, "Tasks Completed: 13")
pdf.drawString(50, 570, "Completion Percentage: 86.67%")

pdf.save()

print(f"PDF created successfully: {output_file}")