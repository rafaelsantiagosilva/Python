print('{:-^50}'.format('Exercício 55'))
maior = 0
menor = 0
for i in range(0, 5):
    peso = float(input(('Digite o peso[kg] da {}º pessoa: ').format(i+1)))
    if i == 0:
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso é {}kg e o menor peso é {}kg.'.format(maior, menor))