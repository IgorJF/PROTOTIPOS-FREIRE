from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Inicializando o navegador
navegador = webdriver.Firefox()
navegador.get("https://web.whatsapp.com")

# Carregando a planilha
planilha = pd.read_excel("pacientes_boleto.xlsx")

# Esperando até que a página carregue completamente
WebDriverWait(navegador, 30).until(EC.presence_of_element_located((By.ID, "side")))

while True:
    try:
        # Esperando até que haja notificações
        WebDriverWait(navegador, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "_ahlk")))
        
        notificacao = navegador.find_elements(By.CLASS_NAME, "_ahlk")
        if len(notificacao) > 0:
            # Clicando na primeira conversa com notificação
            notificacao[0].click()
            
            # Esperando até que a conversa carregue completamente
            WebDriverWait(navegador, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "_amm9")))
            
            todas_mensagens = navegador.find_elements(By.CLASS_NAME, "_amm9")
            ultima_mensagem = todas_mensagens[-1].text if todas_mensagens else ""
            
            if ultima_mensagem.isdigit(): 
                cpf_cliente = ultima_mensagem
                link_boleto = planilha.loc[planilha['CPF'] == int(cpf_cliente), 'Link'].values[0]
                
                if link_boleto: 
                    input_text = navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p")
                    input_text.click()
                    input_text.send_keys(link_boleto)
                    input_text.send_keys(Keys.RETURN)
                else:
                    input_text = navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p")
                    input_text.click()
                    input_text.send_keys("CPF não encontrado. Por favor, verifique o número e tente novamente.")
                    input_text.send_keys(Keys.RETURN)
            else:
                input_text = navegador.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p")
                input_text.click()
                input_text.send_keys("Por favor, envie apenas o CPF para obter o boleto.")
                input_text.send_keys(Keys.RETURN)
        else:
            pass
    except Exception as e:
        print("Erro:", e)
        # Nesse caso, vamos esperar um pouco e tentar novamente
        time.sleep(5)
