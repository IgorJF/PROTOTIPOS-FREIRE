import pyautogui
import time
import mouse
import pandas
import clipboard

pyautogui.PAUSE = 0.5 

pyautogui.press("win")
pyautogui.write("Vivaldi")
pyautogui.press("enter")

time.sleep(3)

link = "http://127.0.0.1:5501/index.html"
pyautogui.click(771,62)
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)
 
#(1764, 901)
#(60,146)
#400, 7
#237, 172
#397, 10

#Nome
pyautogui.tripleClick(60,146) 
pyautogui.hotkey('ctrl', 'c')

#Form
pyautogui.click(497, 14)
pyautogui.click(771,62)
pyautogui.write("https://igorjf.github.io/Teste2/")
pyautogui.press("enter")

#Nome
pyautogui.click(165,214)
pyautogui.hotkey('ctrl', 'v')

pyautogui.click(294, 13)
time.sleep(1)

#Situacao
pyautogui.tripleClick(84, 191) 
pyautogui.hotkey('ctrl', 'c')

pyautogui.click(497, 14)
time.sleep(1)

pyautogui.press("tab")
pyautogui.click(228, 264)
pyautogui.hotkey('ctrl', 'v')

pyautogui.click(294, 13)
time.sleep(1)

#Prova
pyautogui.tripleClick(157,278) 
pyautogui.hotkey('ctrl', 'c')

pyautogui.click(497, 14)
time.sleep(1)

pyautogui.press("tab")
pyautogui.click(212,314)
pyautogui.hotkey('ctrl', 'v')

pyautogui.click(294, 13)
time.sleep(1)

#Coloracao
pyautogui.tripleClick(66, 319) 
pyautogui.hotkey('ctrl', 'c')

pyautogui.click(497, 14)
time.sleep(1)

pyautogui.press("tab")
pyautogui.click(241, 362)
pyautogui.hotkey('ctrl', 'v')

pyautogui.click(294, 13)
time.sleep(1)

#Dente
pyautogui.tripleClick(67, 319) 
pyautogui.hotkey('ctrl', 'c')

pyautogui.click(497, 14)
time.sleep(1)

pyautogui.press("tab")
pyautogui.click(223, 411)
pyautogui.hotkey('ctrl', 'v')

pyautogui.click(294, 13)
time.sleep(1)

#Descricao Geral
pyautogui.tripleClick(151, 364) 
pyautogui.hotkey('ctrl', 'c')

pyautogui.click(497, 14)
time.sleep(1)

pyautogui.press("tab")
pyautogui.click(256, 515)
pyautogui.hotkey('ctrl', 'v')

pyautogui.click(294, 13)
time.sleep(1)

#Descricao sobre Arcada Superior
pyautogui.tripleClick(189, 406) 
pyautogui.hotkey('ctrl', 'c')

pyautogui.click(497, 14)
time.sleep(1)

pyautogui.press("tab")
pyautogui.click(272, 643)
pyautogui.hotkey('ctrl', 'v')

pyautogui.click(294, 13)
time.sleep(1)

#Enviado
pyautogui.tripleClick(127, 536) 
pyautogui.hotkey('ctrl', 'c')

pyautogui.click(497, 14)
time.sleep(1)

pyautogui.press("tab")
pyautogui.click(244, 729)
pyautogui.hotkey('ctrl', 'v')

pyautogui.click(294, 13)
time.sleep(1)

#Recebido
pyautogui.tripleClick(241, 779) 
pyautogui.hotkey('ctrl', 'c')

pyautogui.click(497, 14)
time.sleep(1)

pyautogui.press("tab")
pyautogui.click(241, 779)
pyautogui.hotkey('ctrl', 'v')

pyautogui.press("tab")
pyautogui.press("enter")

# while True:
#     print(mouse.get_position())
#     time.sleep(1)


