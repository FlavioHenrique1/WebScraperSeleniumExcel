import pandas as pd

class Excel:
    def __init__(self):
        self.nome_arquivo = ''
    
    def gravar_em_excel(self, dados_tabela,cabecalho):
        corpo_dados = dados_tabela[1:]  # O restante dos elementos são os dados do corpo
        df = pd.DataFrame(corpo_dados,columns=cabecalho)
        df.to_excel(self.nome_arquivo, index=False)
        print(f'Dados da tabela gravados com sucesso em {self.nome_arquivo}')

