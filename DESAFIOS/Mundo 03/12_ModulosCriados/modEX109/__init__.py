import modEX108
def metade(num,  format=False):
     '''
     Calcula a metade do numero passado
     '''
     if format:
          return modEX108.moeda(num/2)
     else:
          return num/2

def dobro(num, format=False):
     '''
     Calcula o dobro do numero passado
     '''
     if format:
           return modEX108.moeda(num*2)
     else:
          return num*2

def aumentar(num, format=False, porcentagem=10):
     '''
     Calcula o numero + 10% dele mesmo
     '''
     if format:
          return modEX108.moeda(num+(num/100*porcentagem))
     else: 
          return num+(num/100*porcentagem)

def diminuir(num, format=False, porcentagem=10):
     '''
     Calcula o numero - 10% dele mesmo
     '''
     if format:
          return modEX108.moeda(num-(num/100*porcentagem))
     else:
          return num-(num/100*porcentagem)