from random import randint as rand
import time
print(f'{"Exercício 89":-^50}')
print(f'\n{"Mega Sena":=^45}')
#Var
jogos = list()
mega_sena = list()
i=j=0

#Entrada
qtd_jogos = int(input("Quantos jogos você deseja realizar?\nR:"))

#Processamento
while i < qtd_jogos:
     jogos.clear()
     j=0
     while j < 6:
          jogos.append(rand(1, 60))
          j+=1
     mega_sena.append(jogos[:])
     i+=1


#Saída

print('\nOs jogos relizados foram: \n')
print("-"*25, '\n')
for i in range(0, len(mega_sena)):
     time.sleep(0.5)
     print(f'{i+1}º: ', end='')
     for j in range(0, 6):
          print(f'{mega_sena[i][j]} ', end='')
     print('\n')
print("-"*25)