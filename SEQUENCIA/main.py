import openpyxl
from urllib.parse import quote
import webbrowser
from datetime import datetime
import time
import pyautogui

workbook = openpyxl.load_workbook('SEQUENCIA/pacientes.xlsx')
sheet = workbook.active

time.sleep(2)

for cell in sheet['A'][1:]:  
    Numero = cell.value

    mensagem = "Olá, estamos com uma novidade! Se você indicar 3 pessoas, terá a chance de ganhar uma limpeza dentária totalmente grátis! É só enviar o nome e número dessas pessoas bem aqui."

    Numero = str(Numero)
    Numero_limpo = ''.join(filter(str.isdigit, Numero))
    try: 
        link_whatsapp = f"https://web.whatsapp.com/send?phone={Numero_limpo}&text={quote(mensagem)}"
        webbrowser.open(link_whatsapp)
        time.sleep(10) 
        pyautogui.press("enter")
        time.sleep(5)
        pyautogui.hotkey('ctrl','w') 
        time.sleep(2)
    except Exception as e:
        print(f'Erro: {str(e)}')

workbook.close()
