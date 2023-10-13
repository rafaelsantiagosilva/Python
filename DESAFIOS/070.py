print(f'{"Exercício 70":-^50}')
print(f'{"":-^50}\n{"LOJINHA DO VALE":^50}\n{"":-^50}')
nome = nome_maisbarato = ''
opc = 'S'
preco = total = produtos_mais1000 = maisbarato = i = 0
while opc == 'S':
    nome = str(input('Nome do produto: ')).upper()
    preco = float(input('Preço do produto: '))
    total += preco
    if preco > 1000:
        produtos_mais1000+=1
    i+=1
    if i == 1:
        nome_maisbarato = nome
        maisbarato = preco
    if preco < maisbarato:
        nome_maisbarato = nome
        maisbarato = preco
    opc = str(input('Deseja continuar?[S/N]\nR: ')).upper()
print(f'{"":-^50}\n')
print(f'{"INFORMAÇÕES":-^50}')
print(f'O total foi de R${total};')
print(f'Tivemos {produtos_mais1000} produtos que custaram mais de R$1000.00;')
print(f'O produto mais barato foi "{nome_maisbarato}" que custou R${maisbarato}')