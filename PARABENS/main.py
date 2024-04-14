import openpyxl
from urllib.parse import quote
import webbrowser
from datetime import datetime
import os 
import time
import pyautogui

workbook = openpyxl.load_workbook('pacientes_aniversario.xlsx')
sheet = workbook.active

data_atual = datetime.now().date().strftime("%d-%m")

for row in sheet.iter_rows(min_row=2, values_only=True): 
    Nome, Aniversario, Numero = row
    
    aniversario_mes_dia = Aniversario.date().strftime("%d-%m")
    
    if aniversario_mes_dia == data_atual:
        mensagem = f"Olá {Nome}, feliz aniversário! 🎉🎂"

        Numero = str(Numero)
        Numero_limpo = ''.join(filter(str.isdigit, Numero))
        
        link_whatsapp = f"https://web.whatsapp.com/send?phone={Numero_limpo}&text={quote(mensagem)}"
        webbrowser.open(link_whatsapp)
        time.sleep(5) 

        pyautogui.click(804,736)  
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(5) 

workbook.close()

