from random import randint
print('{} {:-^50}{}'.format('\033[1;34m', 'Exercício 58', '\033[m'))
print('{}Olá, sou o seu computador :D\n'.format('\033[0;40m'))
num_comp = randint(0, 10)
print('Acabei de pensar em um número de 0 a 10!\nConsegue adivinhar?')
num_user = int(input('Sugestão: '))
while num_user != num_comp:
    print('\nErrou, eu sabia! Eu sou o mestre dos números!')
    num_user = int(input('Mais alguma sugestão? R: '))
print('\nDroga! Você acertou!')