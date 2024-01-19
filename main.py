import pyautogui
import time 
import pandas as pd 


# COMANDOS PARA AITOMAÇÃO

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
# Iniciando a flask
time.sleep(3)
pyautogui.hotkey("ctrl", "shift", "'") # clicando no arquivo app.py

time.sleep(3)
pyautogui.write("python app.py") # digitando o arquivo onde esta o flask
pyautogui.press("enter") # Iniciando o programa


time.sleep(10) # Tempo para iniciar e preparar o flask
# Script do projeto automação
# Passo 1: Entrar no sistema da empresa    

pyautogui.PAUSE = 0.5

# abrir navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link(endereço ficticio da empresa)
time.sleep(5)
link = "http://127.0.0.1:5000/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5) # Tempo de espera para carregar a página

# Passo 2: fazer login no site
pyautogui.click(x=605, y=440)
# Escrevendo as informções
pyautogui.write("matheus.geffer@gmail.com") # Informar email
pyautogui.press("tab") # Ir para o campo seguinte
pyautogui.write("senha123") # Informar senha
# Enter em logar
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: Importas a base de dados dos prosutos a serem cadastrados
tabela = pd.read_csv("produtos.csv")
#print(tabela) # Visulaizar parte da tabela no terminal

# Passo 4: Preencher os campos com as informações
for linha in tabela.index:
    # Clicar no primeiro campo(código)
    pyautogui.click(x=525, y=229)
    # Inserir as informaçoes do campo código 
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    # Prencher as demais compos
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # Enviar os porduytos preenchidos

    # Subir a tela para o incio da página
    pyautogui.scroll(5000)

    # Final: loop automatico até o cadastro de todos os produtos da tabela


