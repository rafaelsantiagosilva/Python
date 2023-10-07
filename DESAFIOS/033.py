print('{:-^35}'.format('Exercício 33'))
print("Digite 3 números: ")
n1 = float(input())
n2 = float(input())
n3 = float(input())

maior = 0

if n1 > maior:
    maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
    
menor = maior

if n1 < menor:
    menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
    
print("\nMAIOR: {}\nMENOR: {}".format(maior, menor))