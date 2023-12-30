from modEX111 import dado
from modEX111 import moeda
print(f'{"Exercício 112":=^80}')
dinheiro = dado.leiaDinheiro()
print("Dinheiro recebido!")
print("Total: " + moeda.moeda(dinheiro))