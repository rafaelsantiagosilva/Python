print('{:-^50}'.format('Exercício 59'))
n = int(input('Digite um número: '))
fatorial = 1
print('\n')
while n > 0:
    print(n)
    if n != 1:
        print('x')
    fatorial*=n
    n-=1
print('\nO fatorial é de', fatorial)