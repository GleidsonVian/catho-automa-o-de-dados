from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Inicialização do WebDriver
driver = webdriver.Chrome()  # Adicione o caminho para o ChromeDriver se necessário
driver.get('https://www.catho.com.br/')
driver.maximize_window()

# Esperar e interagir com os elementos
try:
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'input-0'))
    )
    search_box.send_keys('analise e desenvolvimento de sistemas')
    submit_button = driver.find_element(By.NAME, 'submit')
    submit_button.click()
    
    # Esperar que os resultados carreguem
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'Header-module__header-wrapper___G5kEL'))
    )
    
    # Capturar e imprimir os elementos
    cards = driver.find_elements(By.CLASS_NAME, 'Header-module__header-wrapper___G5kEL')
    dados = []
    for item in cards:
        dados.append(item.text)  # Armazenar cada item diretamente como texto
        dados.append("")  # Adicionar uma linha em branco

    # Escrever dados em um arquivo de texto
    with open('dados.txt', 'w', encoding='utf-8') as file:
        for linha in dados:
            file.write(linha + "\n")  # Escrever cada linha e adicionar uma quebra de linha
    
    # Imprimir dados para verificação
    print(dados)

finally:
    driver.quit()  # Fechar o navegador
