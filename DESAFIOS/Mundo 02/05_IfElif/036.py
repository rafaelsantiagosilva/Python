print("{:-^35}".format('Exercício 36'))
valor_casa = float(input("Qual é o valor da casa? R$"))
salario_comprador = float(input("Qual é o salário do comprador? R$"))
anos_compra = float(input("Em quantos anos o comprador vai pagar a casa? "))
prestacao_mensal = valor_casa / (anos_compra * 12)
salario_30 = salario_comprador * 0.30
if prestacao_mensal > salario_30:
    print("\nEmpréstimo negado!")
else:
    print('\nEmpréstimo aprovado!')