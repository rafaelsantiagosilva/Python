titulo = "Exercício 12"
print("{:-^40}".format(titulo))
preco =  float(input("Digite o preço do produto: R$"))
percentagem_desconto = 0.05
novo_preco = preco - (preco * percentagem_desconto)
print("\n{:-^30}".format("-"))
print("COM 5% DE DESCONTO:")
print("{:-^30}".format("-"))
print("R${}".format(novo_preco))
print("{:-^30}".format("-"))