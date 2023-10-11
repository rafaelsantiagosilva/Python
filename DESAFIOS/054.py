import datetime
print("{:-^50}".format('Exercício 54'))
ano_atual = datetime.datetime.now().year
maiores=0
menores=0
for i in range(0, 7):
    ano_nasc = int(input('Digite o ano de nascimento da {}º pessoa: '.format(i+1)))
    idade = ano_atual-ano_nasc
    if idade >= 18:
        print('É maior de idade: {}{}{} anos'.format('\033[32m', idade, '\033[m'))
        maiores += 1
    else:
        print('Não é maior de idade: {}{}{} anos'.format('\033[31m', idade, '\033[m'))
        menores += 1
print('\nAo todo, tivemos {}{}{} menores e {}{}{} maiores de idade!'.format('\033[31m', menores, '\033[m', '\033[32m', maiores, '\033[m'))