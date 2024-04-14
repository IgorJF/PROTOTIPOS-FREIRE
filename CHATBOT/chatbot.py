""" 
1 - Receber uma mensagem
2 - Menu de seleção
3 - Escolha

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com")

while True:
    while len(navegador.find_elements(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[3]/div[1]/div/div/div[2]/div")) < 1:
        pass
    
    while len(navegador.find_elements(By.ID, "side")) < 1:
        pass   
    
    notificacao = navegador.find_elements(By.CLASS_NAME, "_ahlk")
    conversa = navegador.find_elements(By.CLASS_NAME, "_ak8k")
    if len(notificacao) > 0:
        conversa[0].click()
        time.sleep(3)
        input_text = navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p")
        input_text.click()
        input_text.send_keys("Olá")
        input_text.send_keys(Keys.RETURN)
    else:
        pass

