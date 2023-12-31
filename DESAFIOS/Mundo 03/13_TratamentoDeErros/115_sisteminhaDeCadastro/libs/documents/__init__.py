from libs.interface import cabecalho

def arquivoExiste(arquivo):
     '''
     Verifica se um arquivo existe, através de seu
     nome passado como parâmetro 
     '''
     try:
          arquivoAberto = open('database/' + arquivo, 'rt') # Read
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
          arquivoCriado = open('database/' + arquivo, 'wt+') # Write, se não existir, cria!
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
          arquivoAberto = open('database/' + arquivo, "rt")
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
          arquivoAberto = open('database/' + arquivo, 'at') # append
     except:
          print(f'\033[31mHouve um erro na abertura do arquivo!\033[m')
     else:
          try:
               arquivoAberto.write(f'{nome}:{idade}\n')
          except:
               print(f'\033Houve um ERRO na hora de escrever os dados!\033[m')