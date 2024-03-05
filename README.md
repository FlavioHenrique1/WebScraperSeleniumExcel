# Especificações do Projeto Web Scraper

## Objetivo
O objetivo deste projeto é criar um web scraper utilizando Selenium para extrair dados de uma tabela em uma página da web e salvá-los em um arquivo Excel.

## Funcionalidades
- Realizar login em uma página web.
- Navegar até uma página contendo uma tabela de dados.
- Extrair os dados da tabela.
- Salvar os dados em um arquivo Excel.

## Ferramentas Utilizadas
- Python 3
- Selenium
- Pandas

## Classes e Métodos

### WebScraper
#### Métodos:
- `executar()`: Método principal que executa o web scraper.
- `interar_dados(driver)`: Método para iterar sobre os dados da tabela e extrair as informações.
- `get_dados_tabela()`: Método para obter os dados da tabela extraídos pelo web scraper.
- `get_cabecalhos()`: Método para obter os cabeçalhos da tabela extraídos pelo web scraper.

### Excel
#### Métodos:
- `gravar_em_excel(dados_tabela, cabecalhos)`: Método para salvar os dados da tabela em um arquivo Excel.

## Fluxo de Execução
1. Inicialização do WebScraper.
2. Realização do login na página web.
3. Navegação até a página com a tabela de dados.
4. Extração dos dados da tabela utilizando Selenium.
5. Salvamento dos dados em um arquivo Excel utilizando Pandas.

## Exemplo de Uso
```python
scraper = WebScraper()
scraper.executar()
dados_tabela = scraper.get_dados_tabela()

excel = Excel()
excel.gravar_em_excel(dados_tabela, scraper.get_cabecalhos())
