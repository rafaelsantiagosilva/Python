print('{:-^50}'.format('Exercício 48'))
print('A soma de todos os números ímpares que são múltiplos de 3 são: ')
for i in range(1, 500):
    if i%2!=0 and i%3==0:
        print(i)