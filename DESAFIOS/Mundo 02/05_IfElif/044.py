print('{:-^50}'.format('Exercício 44'))
preco_normal = float(input('Digite o preço normal do produto: R$'))
preco_mes = ''
print('\n{:-^50}'.format('TIPOS DE PAGAMENTO'))
print('À vista no dinheiro/cheque (10% de desconto) [1]')
print('À vista no cartão (5% de desconto) [2]')
print('Em até 2x no cartão [3]')
print('3x ou mais no cartão (20% de juros simples) [4]')
print('{:-^50}'.format(''))
opc_pagamento = int(input('Digite a opção de pagamento: '))
if opc_pagamento == 1:
    preco_total = preco_normal - (preco_normal * 0.10)
    msg = 'R$' + str(preco_total)
elif opc_pagamento == 2:
    preco_total = preco_normal - (preco_normal * 0.05)
    msg = 'R$' + str(preco_total)
elif opc_pagamento == 3:
    preco_total = preco_normal
    preco_mes = preco_total/2
    msg = 'R$' + str(preco_total) + ' -> R$' + str(preco_mes) + ' por mês!'
elif opc_pagamento == 4:
    meses = int(input('Em quantos meses vai pagar? '))
    preco_total = preco_normal + (preco_normal * 0.20)
    preco_mes = preco_total/meses
    msg = 'R$' + str(preco_total) + ' -> R$' + str(preco_mes) + ' por mês!'
else:
    msg = 'ERRO: Digite uma opção válida!'
print('\n{:-^50}'.format('PREÇO TOTAL'))
print('{:^50}\n{:-^50}'.format(msg, ''))   