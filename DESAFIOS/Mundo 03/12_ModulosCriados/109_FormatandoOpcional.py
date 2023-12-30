from modEX108 import moeda
import modEX109
print(f'{'Exercício 109':=^80}')
preco = float(input('Digite um valor: R$'))
print(f'A metade de {moeda(preco)} é {modEX109.metade(preco, format=True)}')
print(f'O dobro de {moeda(preco)} fica {modEX109.dobro(preco)}')
print(f'Aumentando 10% {moeda(preco)} fica {modEX109.aumentar(preco, format=True)}')
print(f'Diminuindo 10% {moeda(preco)} fica {modEX109.diminuir(preco, format=False)}')