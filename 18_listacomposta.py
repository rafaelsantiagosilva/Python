matriz = list()
dado = list()
opc = 's'
while opc in 'Ss':
    dado.clear()
    dado.append(input('\nDigite o nome: '))
    dado.append(int(input('Digite a idade: ')))
    matriz.append(dado[:])
    opc = input('\nContinuar? [S/N]: ')
print('\nA galera é: \n')
if len(matriz) > 1 and len(dado) > 1:
    for i in range(0, len(dado)):
        for j in range(0, len(matriz)):
            if j % 2 == 0:
                print(f'{matriz[i][j]}', end='')
            else:
                print(f' com {matriz[i][j]} anos.')
else:
    print(f'{matriz[0][0]} com {matriz[0][1]} anos')