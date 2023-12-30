print('{:-^50}'.format('Exercício 61'))
a1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
i=1
print('{:=^35}'.format('10 PRIMEIROS TERMOS DA PA'))
while i <= 10:
    print('{}'.format(a1, razao))
    a1 = a1 + razao
    i+=1
print('{:=^35}'.format(''))