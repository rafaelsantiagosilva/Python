from time import sleep
def leiaNumeroInteiro(texto):
     '''
     Lê um número inteiro e exibe mensagens para erros
     apropriados
     '''
     erroInt = True
     while erroInt:
          try: 
               numero = int(input(texto))
               erroInt = False
               return int(numero)
          except (ValueError, TypeError):
               print('\033[0;31mERRO: Digite um valor inteiro! \033[m')
def linha(tamanho=42):
     '''
     Retorna uma linha a ser desenhada na tela
     '''
     return '-' * tamanho
def cabecalho(texto):
     '''
     Imprime um cabçalho, centralizando o texto
     passado como argumento e tento acima e abaixo
     uma linha() padrão
     '''
     print(linha())
     print(texto.center(42))
     print(linha())
def menu(lista):
     '''
     Recebe uma lista e a imprime na tela como se
     fosse um menu de opções
     '''
     cabecalho('MENU PRINCIPAL')
     contador = 0
     for item in lista:
          print(f'\033[33m{contador+1}\033[m) \033[36m{item}\033[m')
          contador += 1
     print(linha())
     return leiaNumeroInteiro(f'\033[32mSua Opção:\033[m ')
def arquivoExiste(arquivo):
     '''
     Verifica se um arquivo existe, através de seu
     nome passado como parâmetro 
     '''
     try:
          arquivoAberto = open(arquivo, 'rt') # Read
          arquivoAberto.close()

     except FileNotFoundError:
          return False
     else:
          return True
    
def criarArquivo(arquivo):
     '''
     Cria um arquivo na pasta database, com base em 
     seu nome passado como parâmetro
     '''
     try:
          arquivoCriado = open(arquivo, 'wt+') # Write, se não existir, cria!
          arquivoCriado.close()
     except:
          print(f'\033[31mHouve um erro na criação do arquivo!\033[m')
     else:
          print(f'Arquivo {arquivo} criado com sucesso!')
def lerArquivo(arquivo):
     '''
     Lê um arquivo da pasta database
     '''
     try:
          arquivoAberto = open(arquivo, "rt")
     except:
          print(f"\033[31mErro ao ler o arquivo!\033[m")
     else:
          cabecalho('Pessoas Cadastradas')
          for linha in arquivoAberto:
               dado = linha.split(':')
               dado[1] = dado[1].replace('\n', '')
               print(f'{dado[0]:<30}{dado[1]:>3} anos')
def cadastrar(arquivo, nome='desconhecido', idade=0):
     '''
     Cadastra um nome e uma idade no arquivo informado da
     pasta de database
     '''
     try:
          arquivoAberto = open(arquivo, 'at') # append
     except:
          print(f'\033[31mHouve um erro na abertura do arquivo!\033[m')
     else:
          try:
               arquivoAberto.write(f'{nome}:{idade}\n')
          except:
               print(f'\033Houve um ERRO na hora de escrever os dados!\033[m')
arquivo = "cadastro.txt"
if not arquivoExiste(arquivo):
     criarArquivo(arquivo)

while True:
     resposta = menu(['Cadastrar nova pessoa', 'Listar pessoas cadastradas', 'Sair do Sistema'])
     if resposta == 1:
          cabecalho('Novo Cadastro')
          nome = str(input('Nome: '))
          idade = leiaNumeroInteiro(texto="Idade: ")
          cadastrar(arquivo, nome, idade)
          print(linha())
     elif resposta == 2:
           # Opção de listar o conteúdo de um arquivo
          lerArquivo(arquivo)
          print(linha())
     elif resposta == 3:
          cabecalho('Saindo do sistema...Até logo! :D')
          break
     else:
          print(f'\033[0;31mERRO! Digite uma opção válida!\033[m')
          print(linha())
     sleep(1)