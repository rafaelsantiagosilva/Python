import modEX109
from modEX108 import moeda

def resumo(valor, porcentagemA, porcentagemD): 
     print(f'{"=":=^50}\n{"RESUMO DO VALOR":^50}\n{"=":=^50}')
     print("Preço analisado: " + moeda(num=valor))
     print("Dobro do preço: " + modEX109.dobro(num=valor, format=True))
     print("Metade do preço: " + modEX109.dobro(num=valor, format=True))
     print(f"{porcentagemA}% de aumento: {modEX109.aumentar(num=valor, format=True, porcentagem=porcentagemA)}")
     print(f"{porcentagemD}% de desconto: {modEX109.diminuir(num=valor, format=True, porcentagem=porcentagemD)}")
     print(f"{'=':=^50}")