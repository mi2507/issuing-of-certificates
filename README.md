# Emissão de Certificados em Python

Este projeto tem como objetivo gerar certificados personalizados para cursos ou eventos, utilizando a biblioteca **FPDF** e dados provenientes de um arquivo **CSV**.

## Tecnologias Utilizadas

- **Python 3.x**
- **FPDF** (para gerar os arquivos PDF)
- **Pandas** (para ler o arquivo CSV)

## Como Usar

1. **Certifique-se de ter o Python 3.x** instalado na sua máquina.
2. **Instale as dependências do projeto**:
   ```bash
   pip install fpdf pandas

3. **Prepare o arquivo dados.csv. O formato do arquivo deve ser:**

nomecompleto,cargahoraria,data
   
"Alexandre Sauer","200 horas",31 de Janeiro de 2025

"Frederico Sauer","200 horas",31 de Janeiro de 2025

"Andreia de Araujo","200 horas",31 de Janeiro de 2025

"Rafael Jovê","200 horas",31 de Janeiro de 2025

"Heliana Mara","200 horas",31 de Janeiro de 2025

"Michelle Regina","200 horas",31 de Janeiro de 2025

4. **Execute o script app.py:**
   ```bash
   python app.py

5. O script irá gerar os certificados em formato PDF para cada linha de dados no arquivo CSV, com o nome completo, carga horária e data do evento.

## Estrutura do Projeto
app.py: Script principal para gerar os certificados.

dados.csv: Arquivo contendo os dados dos participantes.

template.png: Imagem do modelo de certificado a ser usado no PDF.

certificados/: Pasta onde os certificados gerados serão salvos.


