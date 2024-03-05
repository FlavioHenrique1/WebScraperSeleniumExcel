from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import requests
import pandas as pd
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self):
        self.dados_tabela = []
        self.cabecalhos = []


    def executar(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #Pagina de login
        driver.get("http://10.110.189.11/index.php?page=Login&app=WEBRH")
        #Login do usuario
        elemNome=driver.find_element(By.NAME,"prontuario")
        elemNome.send_keys("148429")
        elemSenha=driver.find_element(By.NAME,"senha")
        elemSenha.send_keys("#Flavio14")
        elemBtn=driver.find_element(By.ID,"entrar")
        elemBtn.click()
        #Pagina do Quadro
        driver.get("http://10.110.189.11/index.php?page=admissao.QuadroLoja")
        elemEmpresa=driver.find_element(By.NAME,"empresa")
        elemEmpresa.send_keys("Americanas SA")
        #Filtros dos Ativos
        sleep(2)
        elemLoja=driver.find_element(By.NAME,"loja")
        elemLoja.send_keys("0150 - Cabo de Santo Agostinho - PE")
        elemBtnFilt=driver.find_element(By.ID,"filtrar")
        elemBtnFilt.click()
        sleep(2)
        #Selecionar o campo das vagas
        elemBtnVagasFix=driver.find_element(By.XPATH,"/html/body/form/div[3]/div/div/ul/li[2]/a")
        elemBtnVagasFix.click()
        # Localize a tabela pelo ID

        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')
        tabela = soup.find('table', attrs={"id":"chamados"}) 
        colunas = tabela.find_all('td')
        print(colunas)

        driver.quit()

    def get_dados_tabela(self):
        return self.dados_tabela

    def get_cabecalhos(self):
        return self.cabecalhos

web_scraper = WebScraper()
web_scraper.executar()
dados_tabela = web_scraper.get_dados_tabela()

# Aqui você pode continuar com o código para gravar os dados em um arquivo Excel
# Certifique-se de que a classe Excel esteja definida como anteriormente
