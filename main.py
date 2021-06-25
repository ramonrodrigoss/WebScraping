from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from IPython.display import display

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

navegador = webdriver.Chrome(options=chrome_options)


#Dizendo para o script que vamos usar o Chrome
#navegador = webdriver.Chrome()

#Pesquisando "Cotacao do dolar"
navegador.get("https://www.google.com/")
navegador.find_element_by_xpath(
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
).send_keys("cotação dolar")
navegador.find_element_by_xpath(
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
).send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
).get_attribute("data-value")

#Pesquisando "Cotacao do euro"
navegador.get("https://www.google.com/")
navegador.find_element_by_xpath(
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
).send_keys("cotação euro")
navegador.find_element_by_xpath(
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
).send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
).get_attribute("data-value")

#Pesquisando "Cotacao do ouro"
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element_by_xpath(
    '//*[@id="comercial"]').get_attribute("value")
cotacao_ouro = cotacao_ouro.replace(",", ".")

#Mostrando as cotacoes
print(cotacao_euro)
print(cotacao_dolar)
print(cotacao_ouro)

#importando planilha para atualizar as cotacoes
tabela = pd.read_excel("Produtos.xlsx")

#alterar a cotacao do Dolar, Euro e Ouro da planinha que importamos
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

