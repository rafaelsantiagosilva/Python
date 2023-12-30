def leiaDinheiro():
     '''
     Lê valores monetários e retorna erros adequados
     '''
     valido = False
     while(valido!=True):
          dinheiro = str(input("Digite um valor monetário: R$")).replace(',', '.')
          if dinheiro.isalpha():
               print(f'\033[0;31mErro: \"{dinheiro}\" é um preço inválido!\033[m')
          else:
               valido = True
               return float(dinheiro)