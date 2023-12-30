from random import randint
print(f'{"Exercício 74":-^50}')
maior = menor = 0
tupla = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print('Os números sorteados foram: ', end='')
for n in range(0, len(tupla)):
    print(f'{tupla[n]}', end='')
    if n != len(tupla)-1:
        print(', ', end='')
    if n == 1:
        maior = tupla[n]
        menor = tupla[n]
    if tupla[n] < menor:
        menor = tupla[n]
    if tupla[n] > maior:
        maior = tupla[n]
print(f'\nO maior foi {maior} e o menor foi o {menor}')