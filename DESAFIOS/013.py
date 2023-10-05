titulo = "Exercício 13"
print("{:-^40}".format(titulo))
salario_antigo =  float(input("Digite o salário atual do funcionário: R$"))
porcentagem_aumento = 0.15
salario_novo = salario_antigo + (salario_antigo * porcentagem_aumento)
print("\n{:-^30}".format("-"))
print("NOVO SALÁRIO:")
print("{:-^30}".format("-"))
print("R${}".format(salario_novo))
print("{:-^30}".format("-"))