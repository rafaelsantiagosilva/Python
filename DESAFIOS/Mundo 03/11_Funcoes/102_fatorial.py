print(f'{'Exercício 102':-^60}')

def fatorial(numero, show):
     resultado = 1
     for i in range(numero, 0, -1):
          resultado *= i
          if show:
               if i != 1:
                    print(f'{i} x ', end='')
               else:
                    print(f'{i} = ', end='')
     return resultado


print(fatorial(5, True))
print(fatorial(4, False))