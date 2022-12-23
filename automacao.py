import pyautogui as py
import pyautogui
import pytesseract as ocr
from PIL import Image
import time
import pygetwindow

dados_conexao = ('DRIVER={Devart ODBC Driver for Oracle};Host=10.1.0.137;Port=1521;SID=DBFESOCONS;UID=GTIC_078463;Password=gtic_sup23_078463;Direct=True')

#Caminho até a automação
py.alert("Atenção! A automação está sendo iniciada.")
py.PAUSE = 1.2

#Acessar onde ficam os dados a serem obtidos
py.moveTo(784, 26)
py.click()
py.moveTo(782, 142)
py.click()
title = "Controle de Recebimentos"

window = pygetwindow.getWindowsWithTitle(title)[0]
if window.title == "Controle de Recebimentos (RDESKAMB.UNIFESO.LAN)":
    py.moveTo(573, 697)
    py.click()
    #Selecionar mês dos resultados
    py.moveTo(325, 392)
    py.click()
    mes = py.write("012021")
    py.moveTo(525, 396)
    py.click()
    #Convenio
    py.moveTo(589, 416)
    py.click()
    py.moveTo(699, 388)
    py.click()
    py.moveTo(836, 427)
    py.click()
    py.moveTo(914, 393)
    py.click()
else:
    py.alert("A janela de Recebimentos não startou. Encerrando...")
    exit()
'''
#Gerador de repetições
contador = 0
while contador <= 8:
    #Variável de Geração de Screenshots
    im = pyautogui.screenshot(f'imagens/image{contador}.png', region=(400,235,54,20))
    time.sleep(1)
    #Variável de processamento de imagens e obtenção de resultado para o sistema 100% testada e funcionando
    phrase = ocr.image_to_string(Image.open(f'imagens/image{contador}.png'), lang='por')
    print(phrase)
    py.alert(phrase)

    py.press('down')
    contador = contador + 1
'''
#Clique na seção de Contas
py.moveTo(610,356)
py.click()
#Dois cliques na Conta a ser conferida
py.moveTo(386, 462)
py.doubleClick()
#recebimento
py.moveTo(479,147)
py.click()


#Alerta de encerramento 
py.alert("A automação foi finalizada. A máquina está liberada pra uso.")
exit()