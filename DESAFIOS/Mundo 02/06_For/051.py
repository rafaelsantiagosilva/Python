print('{:-^50}'.format('Exercício 51'))
a1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('{:=^50}\n{:^50}\n{:=^50}'.format('', '10 PRIMEIROS TERMOS', ''))
for i in range(0, 10):
    print('{}º: {}'.format(i+1, a1))
    a1+=razao
