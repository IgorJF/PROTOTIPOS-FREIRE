import openpyxl
from urllib.parse import quote
import webbrowser
from datetime import datetime
import os 
import time
import pyautogui

workbook = openpyxl.load_workbook('PARABENS/pacientes_aniversario.xlsx')
sheet = workbook.active

data_atual = datetime.now().date().strftime("%d-%m")

for row in sheet.iter_rows(min_row=2, values_only=True): 
    Nome, Aniversario, Numero = row
    
    aniversario_mes_dia = Aniversario.date().strftime("%d-%m")
    
    if aniversario_mes_dia == data_atual:
        mensagem = f"Olá {Nome}, feliz aniversário! 🎉🎂"

        Numero = str(Numero)
        Numero_limpo = ''.join(filter(str.isdigit, Numero))
        try: 
            link_whatsapp = f"https://web.whatsapp.com/send?phone={Numero_limpo}&text={quote(mensagem)}"
            webbrowser.open(link_whatsapp)
            time.sleep(10) 
            pyautogui.press("enter")
            # img = pyautogui.locateCenterOnScreen("PARABENS/seta.png")
            # pyautogui.click(img.x,img.y)
            time.sleep(2)
            pyautogui.hotkey('ctrl','w')
            time.sleep(2)
        except:
           print(f'Não foi possível enviar mensagem para {Nome}')
workbook.close()

