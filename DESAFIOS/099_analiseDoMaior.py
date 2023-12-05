print(f'{'Exercício 99':-^50}')
from time import sleep

def achar_maior(numeros):
     maior = 0
     for n in numeros:
          if n > maior:
               maior = n
     return n

opc = 'S'
numeros = list()
while opc == 'S':
     numeros.append(float(input('Digite um número: ')))
     opc = str(input('Deseja continuar? [S/N]\nR:')).upper()
print('Analisando...')
sleep(1)
print(f'O maior é {achar_maior(numeros=numeros)}')