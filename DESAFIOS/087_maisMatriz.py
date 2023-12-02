print(f'{"Exercício 86":-^50}')
# Var
linha = list()
matriz = list()
i = j = 0
soma_par = soma_terceira_coluna = maior_valor_segunda_linha = 0

#Lendo a matriz
for i in range(0, 3):
     for j in range(0, 3):
          print(f'Digite o valor [{i+1} ,{j+1}]: ', end='')
          linha.append(int(input()))
     matriz.append(linha[:])
     linha.clear()

#Imprimindo a matriz
print('A matriz é: \n')
for i in range(0, 3):
     for j in range(0, 3):
          print(f"{matriz[i][j]} ", end='')
     print('\n')

#Somando os pares
for i in range(0, 3):
     for j in range(0, 3):
          if matriz[i][j] % 2 == 0:
               soma_par+=matriz[i][j]
print(f'A soma de todos os pares é de {soma_par}')

#Somando valores da terceira coluna
for i in range(0, 3):
     soma_terceira_coluna+=matriz[i][2]
print(f'A soma de todos os números da 3ºcoluna é de {soma_terceira_coluna}')

#O maior valor da segunda linha
for i in range(0, 3):
     if maior_valor_segunda_linha < matriz[1][i]:
          maior_valor_segunda_linha = matriz[1][i]
print(f'O maior valor da segunda linha é de {maior_valor_segunda_linha}')
