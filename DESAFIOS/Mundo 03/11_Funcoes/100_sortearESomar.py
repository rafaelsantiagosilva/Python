from random import randint
from time import sleep
print(f'{'Exercício 100':-^50}')

def sortear(lista):
     for i in range(0, 5):
          lista.append(randint(1, 100))

def somar_pares(lista):
     soma = 0
     for i in range(0, len(lista)):
          if lista[i] % 2 == 0:
               soma+=lista[i]
     return soma

print('Os números sorteados foram...')
sleep(0.5)
numeros = list()
sortear(numeros)
print(numeros)

print(f'\nA soma de seus pares é igual a {somar_pares(numeros)}')