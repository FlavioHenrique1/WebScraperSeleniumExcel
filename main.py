import webScraper as ws
import integExcel
import os
from config import MEU_LOGIN, MINHA_SENHA , SITE

def obter_caminho_arquivo(nome_arquivo):
    diretorio_atual = os.path.dirname(__file__)  # Obtém o diretório do script atual
    caminho_completo = os.path.join(diretorio_atual, nome_arquivo)  # Concatena o diretório com o nome do arquivo
    return caminho_completo

# Verifica se o arquivo de destino existe
if os.path.exists(obter_caminho_arquivo("ATIVOS.xlsx")):
    # Substitui o arquivo de destino pelo arquivo de origem
    os.replace(obter_caminho_arquivo("ATIVOS.xlsx"), obter_caminho_arquivo("ATIVOS-OLD.xlsx"))

web_scraper = ws.WebScraper()
web_scraper.site=SITE
web_scraper.executar(site=SITE,login=MEU_LOGIN,senha=MINHA_SENHA)
cabecalhos, dados_tabela = web_scraper.get_dados_tabela()

# Gravar os dados em um arquivo Excel
excel = integExcel.Excel()
excel.nome_arquivo = obter_caminho_arquivo("ATIVOS.xlsx")
excel.gravar_em_excel(dados_tabela, cabecalhos)