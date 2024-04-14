import re
import pdfplumber
import pandas as pd

def extract_info_from_pdf(pdf_path):
    phone_numbers = []
    dates = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            
            phone_matches = re.findall(r'\+\d{2}\d{11}', text)
            phone_numbers.extend(phone_matches)
            
            date_matches = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)
            dates.extend(date_matches)

    return phone_numbers, dates

pdf_path = 'VENCIMENTOS/CONTRATOS.pdf'

phone_numbers, dates = extract_info_from_pdf(pdf_path)

data = {'Número de Telefone': phone_numbers, 'Data de Vencimento': dates}
df = pd.DataFrame(data)

excel_file = 'VENCIMENTOS/contratos.xlsx'
df.to_excel(excel_file, index=False)

