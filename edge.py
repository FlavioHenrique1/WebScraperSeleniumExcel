from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get("http://10.110.189.11/index.php?page=admissao.QuadroLoja")



# Set ativo = Sheets("ativos")
# Application.DisplayAlerts = False

# caminho = "C:\Users\flavio.hsantos\americanas s.a\QUALIDADE-RECIFE - FSB2W03\10. Pessoal\01. Flávio\Ativos"

# FileCopy caminho & "\ATIVOS_LASA_150.xlsx", caminho & "\ATIVOS_LASA_150_OLD.xlsx"

#     ativo.Range("A:M").Value = Empty

# With internet
#     .Get ("http://10.110.189.11/index.php?page=admissao.QuadroLoja")
#     .FindElementByName("prontuario").SendKeys "148429"
#     .FindElementById("senha").SendKeys "#Flavio14"
#     .FindElementById("entrar").Click
#     .Get ("http://10.110.189.11/index.php?page=admissao.QuadroLoja")
#     .FindElementById("empresa").SendKeys "Americanas SA"
#     Application.Wait (Now + TimeValue("0:00:02"))
#     .FindElementById("loja").SendKeys "0150 - Cabo de Santo Agostinho - PE"
#     .FindElementById("filtrar").Click
#     .FindElementByXPath("/html/body/form/div[3]/div/div/ul/li[2]/a").Click
#     .FindElementById("chamados").AsTable.ToExcel ativo.Range("A1")
#     .FindElementByXPath("/html/body/form/div[3]/div/div/ul/li[3]/a").Click
#     cont = WorksheetFunction.CountA(ativo.Range("A:A"))
#     .FindElementByXPath("/html/body/form/div[3]/div/div/div[2]/table[1]").AsTable.ToExcel ativo.Range("a" & cont + 1)
#     cont2 = WorksheetFunction.CountA(ativo.Range("A:A"))
#     ativo.Range("f" & cont + 1 & ":m" & cont2).Value = ativo.Range("e" & cont + 1 & ":l" & cont2).Value
#     ativo.Range("e" & cont & ":e" & cont2).Value = ""
#     .FindElementById("loja").SendKeys "7015 - Cabo de Santo Agostinho - PE"
#     .FindElementById("filtrar").Click
#     .FindElementByXPath("/html/body/form/div[3]/div/div/ul/li[2]/a").Click
#     cont = WorksheetFunction.CountA(ativo.Range("A:A"))
#     .FindElementById("chamados").AsTable.ToExcel ativo.Range("A" & cont + 1)
# End With
    
#     cont = WorksheetFunction.CountA(ativo.Range("A:A"))
#     ativo.Range("A1:M" & cont).Copy
#     Workbooks.Add: ActiveSheet.Paste: Sheets(1).Name = "Planilha1"
#     ActiveWorkbook.SaveAs Filename:=caminho & "\ATIVOS_LASA_150.xlsx", FileFormat:=xlOpenXMLWorkbook, CreateBackup:=False
#     ActiveWindow.Close