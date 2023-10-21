print(f'{"Exercício 79":-^50}')
valores = list()
opc = "S"
while True:
    n = float(input('\nDigite um número: '))
    if n in valores:
        print('Não vou adicionar, valor já encontrado!')
    else:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    opc = input('\nDeseja continuar? [S/N]\nR:').upper()
    if opc != "S":
        break
valores.sort()
print(f'\nEm ordem crescente, os valores ficam: {valores}')