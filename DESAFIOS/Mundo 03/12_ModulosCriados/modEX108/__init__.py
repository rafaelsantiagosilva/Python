def moeda(num=0, moeda="R$"):
     '''
     Formata o número passa como um valor
     em real (R$0,00)
     '''
     return f'{moeda}{num:.2f}'.replace('.', ',')