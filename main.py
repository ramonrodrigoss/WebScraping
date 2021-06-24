from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


#from selenium.webdriver.chrome.options import Options
#chrome_options = Options()
#chrome_options.headless = True
#nav = webdriver.Chrome(options=chrome_options)


#Abrir Navegador
navegador = webdriver.Chrome()
#Abrir o site do Google
navegador.get("https://www.google.com/")
#Pesquisando "Cotacao do dolar" 
navegador.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("cotação dolar")