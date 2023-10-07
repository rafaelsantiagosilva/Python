print('{:-^30}'.format('Exercício 23'))
numero = int(input("Digite um número inteiro [0-9999]: "))
unidade = numero - (numero//10 * 10)
dezena =  numero - (numero//100 * 100) - unidade
centena = numero - (numero//1000 * 1000) - (dezena + unidade)
milhar = numero - (numero//10000 * 10000) - (centena + dezena + unidade)
print("\n{:=^35}\n{:^35}\n{:=^35}".format('', 'DECOMPONDO:', ''))
print("Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(unidade, dezena, centena, milhar))
print('{:=^35}'.format(''))