print(f'{"Exercício 75":-^50}')
n1 = float(input('Digite o 1ºvalor: '))
n2 = float(input('Digite o 2ºvalor: '))
n3 = float(input('Digite o 3ºvalor: '))
n4 = float(input('Digite o 4ºvalor: '))
listaN = [n1, n2, n3, n4]
pares = (0, 0, 0, 0, 0, 0)
qtd9 = 0
pos3 = 0 
for i in range(0, len(listaN)):
    if listaN[i] == 9:
        qtd9+=1
    else:
        qtd9+=0
    if listaN[i] == 3 and pos3 == 0:
        pos3 = i+1
    else:
        pos3 += 0
print(f'{"ANALISE":-^50}')
print(f'=> O 9 apareceu {qtd9} vezes;')
print(f'=> O 3 apareceu pela 1º vez na {pos3}º posição;')
print('Os pares são:')
for i in range(0, len(listaN)):
        if listaN[i] % 2 == 0:
            print(f'-> {listaN[i]}')