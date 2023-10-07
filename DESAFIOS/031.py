print('{:-^35}'.format('Exercício 31'))
distancia = float(input("Qual é a distância da viagem? [km] " ))
if distancia <= 200:
    preco = 0.50 * distancia
else:
    preco = 0.45 * distancia
print("O preço por passagem é igual a: R${}".format(preco))