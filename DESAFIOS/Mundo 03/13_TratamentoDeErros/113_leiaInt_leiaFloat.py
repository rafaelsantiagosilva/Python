print(f'{'Exercício 113':=^50}')

def leiaInt():
     '''
     Lê um número inteiro e exibe mensagens para erros
     apropriados
     '''
     erroInt = True
     while erroInt:
          try: 
               numero = int(input('Digite um número inteiro: '))
               erroInt = False
               return int(numero)
          except (ValueError, TypeError):
               print('\033[0;31mERRO: Digite um valor inteiro! \033[m')

def leiaFloat():
     '''
     Lê um número real e exibe mensagens para erros
     apropriados
     '''
     erroFloat = True
     while erroFloat:
          try: 
               numero = float(input('Digite um número real: '))
               erroFloat = False
               return float(numero)
          except (ValueError, TypeError):
               print('\033[0;31mERRO: Digite um valor real! \033[m')


numeroInteiro = leiaInt()
numeroReal = leiaFloat()