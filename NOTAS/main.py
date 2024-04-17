import openpyxl
from urllib.parse import quote
import webbrowser
from datetime import datetime
import time
import pyautogui

workbook = openpyxl.load_workbook('NOTAS/pacientes.xlsx')
sheet = workbook.active

data_atual = datetime.now().date().strftime("%d-%m")

time.sleep(2)

for row in sheet.iter_rows(min_row=2, values_only=True): 
    Nome, Numero, Dentista = row
    
    mensagem = f"Olá {Nome}, bom dia, de 0 a 10, qual a nota você dá para o atendimento do {Dentista}?"

    Numero = str(Numero)
    Numero_limpo = ''.join(filter(str.isdigit, Numero))
    try: 
        link_whatsapp = f"https://web.whatsapp.com/send?phone={Numero_limpo}&text={quote(mensagem)}"
        webbrowser.open(link_whatsapp)
        time.sleep(5) 
        pyautogui.press("enter")
        time.sleep(5)
        pyautogui.hotkey('ctrl','w') 
        time.sleep(2)
    except Exception as e:
        print(f'Não foi possível enviar mensagem para {Nome}: {str(e)}')

workbook.close()
