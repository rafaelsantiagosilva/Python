def moeda(num=0, moeda="R$"):
     '''
     Formata o número passa como um valor
     em real (R$0,00)
     '''
     return f'{moeda}{num:.2f}'.replace('.', ',')

def metade(num,  format=False):
     '''
     Calcula a metade do numero passado
     '''
     if format:
          return moeda(num/2)
     else:
          return num/2

def dobro(num, format=False):
     '''
     Calcula o dobro do numero passado
     '''
     if format:
           return moeda(num*2)
     else:
          return num*2

def aumentar(num, format=False, porcentagem=10):
     '''
     Calcula o numero + 10% dele mesmo
     '''
     if format:
          return moeda(num+(num/100*porcentagem))
     else: 
          return num+(num/100*porcentagem)

def diminuir(num, format=False, porcentagem=10):
     '''
     Calcula o numero - 10% dele mesmo
     '''
     if format:
          return moeda(num-(num/100*porcentagem))
     else:
          return num-(num/100*porcentagem)
     
def resumo(valor, porcentagemA, porcentagemD): 
     '''
     Apresenta um resumo usando as funções dos módulos
     desenvolvidos nos outros exercícios
     '''
     print(f'{"=":=^50}\n{"RESUMO DO VALOR":^50}\n{"=":=^50}')
     print("Preço analisado: " + moeda(num=valor))
     print("Dobro do preço: " + dobro(num=valor, format=True))
     print("Metade do preço: " + dobro(num=valor, format=True))
     print(f"{porcentagemA}% de aumento: {aumentar(num=valor, format=True, porcentagem=porcentagemA)}")
     print(f"{porcentagemD}% de desconto: {diminuir(num=valor, format=True, porcentagem=porcentagemD)}")
     print(f"{'=':=^50}")