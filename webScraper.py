from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

class WebScraper:
    def __init__(self):
        self.dados_tabela = []
        self.cabecalhos = []
    def interar_dados(self, tabela):

        # Obtenha todas as linhas da tabela
        linhas = tabela.find_elements(By.TAG_NAME, 'tr')
        # Obtenha os cabeçalhos da tabela (se houver)
        cabecalho_linha = linhas[0]
        celulas_cabecalho = cabecalho_linha.find_elements(By.TAG_NAME, 'th')
        if celulas_cabecalho:
            # Se houver células de cabeçalho, extraia o texto delas
            self.cabecalhos = [celula.text for celula in celulas_cabecalho]
            # Adicione os cabeçalhos à lista de dados da tabela
            self.dados_tabela.append(self.cabecalhos)

        # Itere sobre as linhas e imprima o texto de cada célula
        for linha in linhas[1:]:

            # Obtenha todas as células da linha
            celulas = linha.find_elements(By.TAG_NAME, 'td')

            
            if (len(celulas) > 12):
                i=0
            else:
                i=1

            id=celulas[0].text
            empresa=celulas[1].text
            loja=celulas[2].text
            cCusto=celulas[3].text
            descCCusto=celulas[4].text
            pront=celulas[5].text
            cpf=celulas[6-i].text
            nome=celulas[7-i].text
            telFix=celulas[8-i].text
            telCel=celulas[9-i].text
            adms=celulas[10-i].text
            cargo=celulas[11-i].text
            vaga=celulas[12-i].text

            # Inicialize uma lista para armazenar os dados da linha
            dados_linha = [id,empresa,loja,cCusto,descCCusto,pront,cpf,nome,telFix,telCel,adms,cargo,vaga]

            # # Inicialize uma lista para armazenar os dados da linha
            # dados_linha = [celula.text for celula in celulas]
            # Adicione os dados da linha à lista de dados da tabela
            self.dados_tabela.append(dados_linha)

    def executar(self,site,login,senha):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #Pagina de login
        driver.get(site)
        #Login do usuario
        elemNome=driver.find_element(By.NAME,"prontuario")
        elemNome.send_keys(login)
        elemSenha=driver.find_element(By.NAME,"senha")
        elemSenha.send_keys(senha)
        elemBtn=driver.find_element(By.ID,"entrar")
        elemBtn.click()
        #Pagina do Quadro
        driver.get(site)
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
        tabela = driver.find_element(By.ID,'chamados')
        #Chamar a função para interar os dados
        self.interar_dados(tabela)

        elemBtnVagasTemp=driver.find_element(By.XPATH,"/html/body/form/div[3]/div/div/ul/li[3]/a")
        elemBtnVagasTemp.click()
        sleep(2)
        # Localize a tabela pelo ID
        tabela = driver.find_element(By.XPATH,'/html/body/form/div[3]/div/div/div[2]/table[1]')
        self.interar_dados(tabela)

        elemLoja=driver.find_element(By.NAME,"loja")
        elemLoja.send_keys("7015 - Cabo de Santo Agostinho - PE")

        elemBtnFilt=driver.find_element(By.ID,"filtrar")
        elemBtnFilt.click()

        #Selecionar o campo das vagas
        elemBtnVagasFix=driver.find_element(By.XPATH,"/html/body/form/div[3]/div/div/ul/li[2]/a")
        elemBtnVagasFix.click()
        # Localize a tabela pelo ID
        tabela = driver.find_element(By.XPATH,'/html/body/form/div[3]/div/div/div[1]/table[1]')
        self.interar_dados(tabela)

        driver.quit()

    def get_dados_tabela(self):
        return self.cabecalhos, self.dados_tabela

# Aqui você pode continuar com o código para gravar os dados em um arquivo Excel
# Certifique-se de que a classe Excel esteja definida como anteriormente
