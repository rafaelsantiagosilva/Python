from modEX110 import resumo
preco = float(input("Digite o preço[0.00]: "))
porcentagemAumento = float(input("Digite a porcentagem de aumento[%]: "))
porcentagemDesconto = float(input("Digite a porcentagem de desconto[%]: "))
resumo(valor=preco, porcentagemA=porcentagemAumento, porcentagemD=porcentagemDesconto)