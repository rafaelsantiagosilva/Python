from libs import interface
from libs import documents
from time import sleep

arquivo = "cadastro.txt"
if not documents.arquivoExiste(arquivo):
     documents.criarArquivo(arquivo)

while True:
     resposta = interface.menu(['Cadastrar nova pessoa', 'Listar pessoas cadastradas', 'Sair do Sistema'])
     if resposta == 1:
          interface.cabecalho('Novo Cadastro')
          nome = str(input('Nome: '))
          idade = interface.leiaNumeroInteiro(texto="Idade: ")
          documents.cadastrar(arquivo, nome, idade)
          print(interface.linha())
     elif resposta == 2:
           # Opção de listar o conteúdo de um arquivo
          documents.lerArquivo(arquivo)
          print(interface.linha())
     elif resposta == 3:
          interface.cabecalho('Saindo do sistema...Até logo! :D')
          break
     else:
          print(f'\033[0;31mERRO! Digite uma opção válida!\033[m')
          print(interface.linha())
     sleep(1)
