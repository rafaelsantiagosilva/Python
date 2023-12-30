print('{:-^50}'.format('Exercício 62'))
a1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
i=1
print('{:=^50}'.format('10 PRIMEIROS TERMOS DA PA'))
while i <= 10:
    print(a1)
    a1+=razao
    i+=1
opc = 1
while opc != 0:
    opc = int(input('\nPAUSA! Quantos termos vc deseja mostrar a mais?\nR:'))
    for j in range(0, opc):
        print(a1)
        a1+=razao
print('{:=^50}'.format(''))