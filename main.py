"""
NOME DO PROGRAMA: Projeto de Automação de cadastro de produtos

VERSÃO 1.0

SINTAXE: Educacional

DESCRIÇÃO: O software tem como objetivo simular o funcionamento da alocação de memoria
que os sistemas operacionais fazem automaticamente, esse projeto foi pensado para deixar mais claro
a como os processos sao alocados e redistribuidos na memoria de um computador.

LINGUAGENS BACKEND: Python

LINGUAGENS FRONTEND: Javascript, HTML & CSS 

FRAMEWORKS: Flask

SISTEMAS OPERACIONAIS: Software roda via web logo nao temos nenhuma restrição para OS.

REQUISITOS: Acesso a internet pois o bootstrap utiliza seus repositorio.

AUTOR: Matheus Tomas Geffer

CRIAÇÃO: 15/01/2024

ALTERAÇÕES: 09/05/2023 - Adicionado visual na pagina web
            10/05/2023 - Correções de bugs
            16/05/2023 - Testes de QA(Aprovado)
    
            
TODAS AS BILIOTECAS UTILIZADAS ESTÃO LOCALIZADAS NO ARQUIVO requirements.txt | Para que sejam importadas deve-se utilizar o seguinte comando no terminal "pip install --requirements.txt"
"""


"""

Importação das bibliotecas que serão utilizadas

"""

import pyautogui
import time 
import pandas as pd 


"""  COMANDOS PARA AUTOMAÇÃO

 pyautogui.write -> escrever um texto
 pyautogui.press -> apertar 1 tecla
 pyautogui.click -> clicar em algum lugar da tela
 pyautogui.hotkey -> combinação de teclas """

time.sleep(3)
pyautogui.hotkey("ctrl", "shift", "'") # Atalho para abrir novo terminal

time.sleep(3)
pyautogui.write("python app.py") # Digitando o arquivo onde esta o flask
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
pyautogui.write("name_user@projeto.com") # Informar email
pyautogui.press("tab") # Ir para o campo seguinte
pyautogui.write("senha123") # Informar senha
# Enter em logar
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: Importas a base de dados dos prosutos a serem cadastrados
tabela = pd.read_csv("produtos.csv")

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
    pyautogui.press("enter") # Enviar os pordutos preenchidos

    # Subir a tela para o incio da página
    pyautogui.scroll(5000)

    # Final: loop automatico até o cadastro de todos os produtos da tabela


