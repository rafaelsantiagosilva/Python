print(f'{'Exercício 98':-^70}')
from time import sleep

def contador(inicio, fim, passo):
     if inicio < fim:
          for i in range(inicio, fim+1, passo):
               sleep(0.5)
               print(i)
     elif inicio > fim:
          for i in range(inicio, fim-1, -passo):
               sleep(0.5)
               print(i)
     else:
          print(inicio)

inicio = int(input('Digite o número que deseja iniciar a sequência: '))
passo = int(input('Digite o passo da sequência: '))
fim = int(input('Digite onde deseja que a sequência termine: '))
print('\nContando:')
contador(inicio=inicio, passo=passo, fim=fim)