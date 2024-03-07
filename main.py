import pyautogui
import time
import pandas
tabela = pandas.read_csv("produtos.csv")
pyautogui.press("win")
pyautogui.write("chrome")
#pyautogui.hotkey("ctrl", "c")
pyautogui.press("enter")
time.sleep(0.2)

pyautogui.press('tab')
pyautogui.press("enter")
time.sleep(0.2)

link="https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email="pythonimpressionador@gmail.com"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(0.2)


pyautogui.click(x=878, y=374)
pyautogui.write(email)

pyautogui.press('tab')
pyautogui.write("senha")

pyautogui.press('tab')
pyautogui.press("enter")
time.sleep(2.5)

for linha in tabela.index:
    pyautogui.click(x=888, y=257)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press('tab')

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press('tab')

    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press('tab')

    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press('tab')

    obs = tabela.loc[linha, "obs"]
    #Se o campo não estiver vazio
    if not pandas.isna(obs):
        pyautogui.write(obs)
    
    pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.scroll(5000)

