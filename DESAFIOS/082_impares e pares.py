print(f'{"Exercício 82":-^50}')
numeros = list()
pares = list()
impares = list()
opc = 'S'
while opc == 'S':
    n = int(input('\nDigite um número: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    opc = str(input('\nQuer continuar? [S/N]\nR:')).upper()
print(f'\nOs números digitados foram: \n{numeros}')
print(f'\nOs números ímpares digitados foram: \n{impares}')
print(f'\nOs números pares digitados foram: \n{pares}') 