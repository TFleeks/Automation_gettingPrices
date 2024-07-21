# importar as bibliotecas especificas

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# abrir o navegador

driver = webdriver.Chrome()
driver.get("https://www.google.com/")


# pesquisar e extrair a cotação do dolar

driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys('Cotação Dólar')
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys(Keys.ENTER)
cotacao_dolar = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(f"Atualmente, o Dólar está no valor de { cotacao_dolar }")


# pesquisar e extrair a cotação do euro

driver.get("https://www.google.com")
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys('Cotação Euro')
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys(Keys.ENTER)
cotacao_euro = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(f"Já o valor do Euro está { cotacao_euro }")

# Finalizar o navegador

driver.quit()