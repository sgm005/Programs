from fpdf import FPDF

# Data for the resume
name = "Manuel Alejandro Sánchez Moreno"
email = "manuel.alejandro.sanchez2000@gmail.com"
phone = "+34 616616438"
linkedin = "www.linkedin.com/in/manuel-alejandro-sánchez-moreno-a79aab196"
github = "https://github.com/sgm005"

# Creating the PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, f"{name}", ln=True, align='C')

# Contact Information
pdf.set_font("Arial", "I", 12)
pdf.cell(200, 10, "Contact", ln=True, align='L')
pdf.set_font("Arial", "", 12)
pdf.cell(200, 10, f"Email: {email}", ln=True, align='L')
pdf.cell(200, 10, f"Phone: {phone}", ln=True, align='L')
pdf.cell(200, 10, f"LinkedIn: {linkedin}", ln=True, align='L')
pdf.cell(200, 10, f"GitHub: {github}", ln=True, align='L')

# Professional Summary
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "\nProfessional Summary", ln=True, align='L')
pdf.set_font("Arial", "", 12)
summary_text = (
    "Industrial engineer in the process of transitioning to programming, "
    "with a solid technical background and specialization in Python. Recently, "
    "I have completed 3 months of experience as a remote programmer at SANDAV in Madrid. "
    "I have a high proficiency in English (C1) and French (B2), I am a fast learner, perfectionist, "
    "and I perform effectively under pressure."
)
pdf.multi_cell(0, 10, summary_text)

# Work Experience
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "\nWork Experience", ln=True, align='L')
pdf.set_font("Arial", "B", 12)
pdf.cell(200, 10, "Junior Programmer (Remote)", ln=True, align='L')
pdf.set_font("Arial", "", 12)
pdf.cell(200, 10, "SANDAV - Madrid, Spain", ln=True, align='L')
pdf.cell(200, 10, "Jan 2023 - Mar 2023", ln=True, align='L')
experience_text = (
    "- Developed and maintained applications in Python, optimizing processes and improving code efficiency.\n"
    "- Participated in automation projects, utilizing libraries like Pandas and BeautifulSoup for data processing and analysis."
)
pdf.multi_cell(0, 10, experience_text)

# Technical Skills
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "\nTechnical Skills", ln=True, align='L')
pdf.set_font("Arial", "", 12)
skills_text = (
    "- Programming Languages: Python (proficient in libraries such as Pandas, NumPy, and Requests), basic knowledge of SQL.\n"
    "- Tools and Technologies: Git, Visual Studio Code, Jupyter.\n"
    "- Additional Skills: Fast learner, committed, and able to work well under pressure."
)
pdf.multi_cell(0, 10, skills_text)

# Save the PDF
pdf_file_path = "Curriculum_Manuel_Sanchez_Moreno_Enhanced.pdf"  # Specify the output path
pdf.output(pdf_file_path)

print(f"PDF generated and saved as {pdf_file_path}")
