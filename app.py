from fpdf import FPDF
import pandas as pd

# Carregar dados do CSV
dados = pd.read_csv("dados.csv")

# Dados do certificado
titulo = "CERTIFICADO"
subtitulo = "O Diretor da Institução SIMPLIFICA,no uso de suas atribuições"
texto2 = "confere o presente certificado a:"
texto3 = "por ter concluído em 2025 o curso"
texto4 = "Analista de Dados | Power BI"

# Loop para criar o certificado de cada pessoa
for i, row in dados.iterrows():
    nome = row['nomecompleto']
    cargahoraria = row['cargahoraria']
    data = row['data']
    
    pdf = FPDF()
    pdf.add_page()
    
    pdf.image("template.png", x=0, y=0)
    
    
    # Adicionar o texto no certificado
    pdf.set_font("Arial", 'B', size=26)
    pdf.set_text_color(33, 24, 136)
    pdf.text(74, 105, titulo)

    pdf.set_font("Arial", '', size=12)
    pdf.set_text_color(0, 102, 204)
    pdf.text(34, 128, subtitulo)
    pdf.text(34, 138, texto2)

    # Adicionar nome completo, e-mail e data
    pdf.set_font("Times", 'BI', size=24)
    pdf.set_text_color(33, 24, 136)
    pdf.text(75, 160, nome)

    pdf.set_font("Arial", '', size=10)
    pdf.set_text_color(0, 102, 204)
    pdf.text(75, 174, texto3)

    pdf.set_font("Arial", 'B', size=13)
    pdf.set_text_color(0, 102, 204)
    pdf.text(70, 180, texto4)
    
    # Adicionar carga horaria e data no PDF (ajustar as coordenadas conforme necessário)
    pdf.set_font("Arial", '', size=10)
    pdf.set_text_color(0, 102, 204)
    pdf.text(20, 200, f"Carga Horária: {cargahoraria}")

    pdf.set_font("Arial", '', size=10)
    pdf.set_text_color(0, 102, 204)
    pdf.text(136, 200, f"São Paulo,{data}.")

    # Salvar o PDF com um nome de arquivo único
    pdf.output(f"Certificado_{nome}.pdf")
