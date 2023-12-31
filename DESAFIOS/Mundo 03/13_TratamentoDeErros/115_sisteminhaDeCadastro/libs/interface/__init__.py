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