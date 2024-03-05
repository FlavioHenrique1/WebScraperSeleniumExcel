import pandas as pd

class Excel:
    def __init__(self):
        self.nome_arquivo = 'C:\\Users\\flavio.hsantos\\Documents\\dados_tabela.xlsx'
    
    def gravar_em_excel(self, dados_tabela):
        cabecalhos = dados_tabela[0]  # O primeiro elemento é o cabeçalho
        corpo_dados = dados_tabela[1:]  # O restante dos elementos são os dados do corpo
        df = pd.DataFrame(corpo_dados)
        df.to_excel(self.nome_arquivo, index=False)
        print(f'Dados da tabela gravados com sucesso em {self.nome_arquivo}')

