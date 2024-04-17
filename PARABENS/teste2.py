import openpyxl
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

workbook = openpyxl.load_workbook('PARABENS/pacientes_aniversario.xlsx')
sheet = workbook.active

data_atual = datetime.now().date().strftime("%d-%m")

caminho_audio = "C:/Users/igorj/Documents/MEU/PROJETOS/PROTÓTIPOS FREIRE/PARABENS/teste.mp3"

navegador = webdriver.Firefox()
navegador.get("https://web.whatsapp.com")

time.sleep(30)

def enviar_audio(numero):
    link_whatsapp = f"https://web.whatsapp.com/send?phone={numero}"
    navegador.get(link_whatsapp)
    time.sleep(30)  
    input_box = navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div/div/div/div/span/svg/path")
    input_box.click()
    time.sleep(2)
    input_box.send_keys(caminho_audio)
    time.sleep(2)
    input_box.send_keys(Keys.RETURN)

for row in sheet.iter_rows(min_row=2, values_only=True): 
    Nome, Aniversario, Numero = row
    
    aniversario_mes_dia = Aniversario.date().strftime("%d-%m")
    
    if aniversario_mes_dia == data_atual:
        Numero = str(Numero)
        Numero_limpo = ''.join(filter(str.isdigit, Numero))
        try: 
            enviar_audio(Numero_limpo)
            print(f'Áudio enviado para {Nome}')
        except Exception as e:
            print(f'Erro ao enviar áudio para {Nome}: {str(e)}')

navegador.quit()
workbook.close()
