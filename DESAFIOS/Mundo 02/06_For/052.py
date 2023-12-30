import sys
print('{:-^50}'.format('Exercício 52'))
div = 0
opc = 'S'
while opc == 'S':
    div = 0
    print('\n{:=^50}'.format('DIVISORES'))
    n = int(input('Digite um número: '))
    for i in range(1, n+1):
        if n % i == 0:
            div+=1
            print('\033[34m', end="")
            if div > 2:
                resp = 'NÃO É PRIMO!'
            else:
                resp = 'É PRIMO!'
        else:
            div+=0
            print('\033[37m', end="")
        sys.stdout.write('{} '.format(i, end=""))
    print('\n{}{:=^50}'.format('\033[m', ''))
    print('O número {} {}'.format(n, resp))
    opc = str(input('\nQuer continuar? [S/N]\nR: ')).upper()