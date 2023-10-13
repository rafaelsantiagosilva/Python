print('{:-^50}'.format('Exercício 59'))
v1 = float(input('Digite o 1º valor: '))
v2 = float(input('Digite o 2º valor:'))

continuar = True
while continuar:
    print('\n{:=^25}'.format('M E N U'))
    print('Somar[1]\nSubtrair[2]\nMultiplicar[3]\nDividir[4]\nSair[5]')
    print('{:=^25}'.format(''))
    opc = int(input('\nO que você deseja fazer?\nR:'))
    if opc == 1:
        res = v1+v2
        print('n\Resultado:', res)
    elif opc == 2:
        res = v1-v2
        print('\nResultado:', res)
    elif opc == 3:
        res = v1*v2
        print('\nResultado:', res)
    elif opc == 4:
        res = v1/v2
        print('\nResultado:', res)
    else:
        continuar = False
        print('\nTchau Tchau!')
    
