print('{:-^35}'.format('Exercício 34'))
salario = float(input("Digite o salário: R$"))
if salario > 1250:
    novo_salario = salario + (salario * 0.10)
else:
    novo_salario = salario + (salario * 0.15)
print("NOVO SALÁRIO: R$", novo_salario)