print('{:-^50}'.format('Exercício 64'))
n = 1
contador = soma = 0
while n != 0:
    n = int(input('Digite um número[0 para parar]: '))
    if n != 0:
        contador += 1
        soma += n
print('A soma dos {} números digitados foi de {}'.format(contador, soma))