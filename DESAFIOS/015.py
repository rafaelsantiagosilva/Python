print("{:-^30}".format('Exercício 15'))
km_percorridos = float(input("Quantos km foram percorridos? "))
dias = int(input("E ele foi alugado por quantos dias? "))
preco = (60 * dias) + (0.15 * km_percorridos)
print("\n{:=^30}\n{:^30}\n{:=^30}".format('', "O PREÇO A PAGAR É DE:", ''))
print("R${:.2f}\n{:=^30}".format(preco, ''))