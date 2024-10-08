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
pdf.cell(200, 10, "Contacto", ln=True, align='L')
pdf.set_font("Arial", "", 12)
pdf.cell(200, 10, f"Email: {email}", ln=True, align='L')
pdf.cell(200, 10, f"Teléfono: {phone}", ln=True, align='L')
pdf.cell(200, 10, f"LinkedIn: {linkedin}", ln=True, align='L')
pdf.cell(200, 10, f"GitHub: {github}", ln=True, align='L')

# Professional Summary
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "\nResumen Profesional", ln=True, align='L')
pdf.set_font("Arial", "", 12)
summary_text = (
    "Ingeniero industrial en proceso de reconversión hacia la programación, "
    "con una sólida base técnica y especialización en Python. Recientemente, "
    "he completado 3 meses de experiencia como programador remoto en SANDAV, Madrid. "
    "Cuento con un alto dominio de inglés (C1) y francés (B2), soy un aprendiz rápido y perfeccionista, "
    "y me desenvuelvo con efectividad bajo presión."
)
pdf.multi_cell(0, 10, summary_text)

# Work Experience
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "\nExperiencia Laboral", ln=True, align='L')
pdf.set_font("Arial", "B", 12)
pdf.cell(200, 10, "Programador Junior (Remoto)", ln=True, align='L')
pdf.set_font("Arial", "", 12)
pdf.cell(200, 10, "SANDAV - Madrid, España", ln=True, align='L')
pdf.cell(200, 10, "Ene 2023 - Mar 2023", ln=True, align='L')
experience_text = (
    "- Desarrollé y mantuve aplicaciones en Python, optimizando procesos y mejorando la eficiencia del código.\n"
    "- Participé en proyectos de automatización, manejando bibliotecas como Pandas y BeautifulSoup para el procesamiento y análisis de datos."
)
pdf.multi_cell(0, 10, experience_text)

# Technical Skills
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "\nHabilidades Técnicas", ln=True, align='L')
pdf.set_font("Arial", "", 12)
skills_text = (
    "- Lenguajes de Programación: Python (manejo de librerías como Pandas, NumPy y Requests), conocimientos básicos en SQL.\n"
    "- Herramientas y Tecnologías: Git, Visual Studio Code, Jupyter."
)
pdf.multi_cell(0, 10, skills_text)

# Save the PDF
pdf_file_path = "Curriculum_Manuel_Sanchez_Moreno.pdf"  # Specify the output path
pdf.output(pdf_file_path)

print(f"PDF generated and saved as {pdf_file_path}")