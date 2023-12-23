import modEX107
import modEX108
print(f'{'Exercício 108':=^80}')
num = float(input("Digite um número: "))
print("O seu dobro é", modEX108.moeda(modEX107.dobro(num)))
print("A sua metade é", modEX108.moeda(modEX107.metade(num)))
print("Aumentando em 10% fica", modEX108.moeda(modEX107.aumentar(num)))
print("Diminuindo em 10% fica", modEX108.moeda(modEX107.diminuir(num)))
