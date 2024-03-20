# Passo a Passo do projeto
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyauogui
import pyautogui
import time

pyautogui.PAUSE = 1 #configuração de pausa a cada comando

# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar 1 tecla do teclado
# pyautogui.hotkey("ctrl", v") -> combinação de teclas

# abrir o navegador (chrome)
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press('enter')

# dar uma pausa um pouco maior (3 segundos)
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=656, y=510, clicks=1, button='right')
pyautogui.write('trechds@gmail.com')

# escreva a senha
pyautogui.press('tab')
pyautogui.write('123456789')

# clicar no botão de logar
pyautogui.click(x=950, y=716, clicks=1, button='right')
time.sleep(3)

# Passo 3: Importar a base de dados
# pip install pandas numpy openpyxl
import pandas
tabela = pandas.read_csv('produtos.csv')
print(tabela)

# Passo 4: Cadastras 1 produto
# para cada linha da minha tabela
for linha in tabela.index:                       # index para linhas, e colmumns para  colunas
    # clicar no 1º campo
    pyautogui.click(x=686, y=364)
    # codigo do produto
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(tabela.loc[linha, 'codigo'])
    pyautogui.press('tab')
    # marca
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    # tipo
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    # cateroria
    # str() string -> texto
    # str(1) -> 1 -> '1'
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    # preço
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    # custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    # obs
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):          # isna (na, nan) signifia está vazio
        pyautogui.write(obs)
    pyautogui.press('tab')
    # enviar
    pyautogui.press('enter')
    pyautogui.scroll(5000)           # número positivo é pra cima, e número negativo é pra baixo

# Passo 5: Repetir o processo de adastro até acabar a base de dados

# def cadastrar_protudo()
    