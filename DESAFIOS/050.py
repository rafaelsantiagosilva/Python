print('{:-^50}'.format('Exercício 50'))
print('Insira 6 números: ')
s=0
for i in range(0, 6):
    n = int(input('{}º: '.format(i+1)))
    if n % 2 == 0:
        s+=n
    else:
        s+=0
print('A soma dos números pares digitados é de:', s)