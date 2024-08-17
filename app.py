# importar as bibliotecas especificas

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# abrir o navegador
driver = webdriver.Chrome()


# Função para pegar o dólar
def getDolar():
    # abrindo o navegador na pagina do google para realizar a pesquisa
    driver.get("https://www.google.com/")

    # pesquisar e extrair a cotação do dolar
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys('Cotação Dólar')

    # apertando enter para pesquisar
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys(Keys.ENTER)

    # pegando o valor preciso da cotação do dólar
    cotacao_dolar = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

    # mostrando exatamente o valor do dolar para o usuario caso queira ele precisamente
    print(f"Atualmente, o Dólar está no valor de { cotacao_dolar }")

# Função para pegar o euro
def getEuro():
    # abrindo o navegador na pagina do google para realizar a pesquisa
    driver.get("https://www.google.com")

    # pesquisando a cotação do euro
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys('Cotação Euro')
    
    # apertando enter para prosseguir com a pesquisa
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys(Keys.ENTER)
    
    # pegando o valor preciso da cotação do dolar
    cotacao_euro = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
    
    # mostrando exatamente o valor do euro para o usuario caso ele queira precisamente
    print(f"Já o valor do Euro está { cotacao_euro }")

getDolar()
getEuro()


# Finalizar o navegador

driver.quit()
