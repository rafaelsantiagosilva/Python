print('{:-^50}'.format('Exercício 49'))
n = int(input('Digite um número: '))
m = int(input('Até que número você deseja que apareça a tabuada? '))
print('{:=^50}\n{:^50}\n{:=^50}'.format('', 'TABUADA', ''))
for i in range(0, m+1):
    print('{} X {} = {}'.format(n, i, n*i))
print('{:=^50}'.format(''))