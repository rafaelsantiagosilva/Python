print('{:-^50}'.format('Exercício 65'))
opc = True
qtd = media = maior = menor = 0
while opc:
    num = float(input('Digite um número: '))
    qtd+=1
    media += num
    if qtd == 1:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    opc = str(input('Quer continuar?[S/N]\nR:')).upper()
    if opc != 'S':
        opc = False
media/=qtd
print('\n{:-^50}'.format('INFORMAÇÕES'))
print('A média dos {} números foi de {}.'.format(qtd, media))
print('E o maior número foi {} e o menor foi {}.'.format(maior, menor))