import datetime
print("{:-^40}".format('Exercício 39'))
ano_atual = datetime.datetime.now().year
ano_nasc = int(input('Digite o seu ano de nascimento: '))
idade = ano_atual - ano_nasc
print('Você tem {} anos!'.format(idade))
print('{:-^40}'.format('Alistamento'))
if idade < 18:
    print('Você vai se alistar daqui {} anos!'.format(18-idade))
elif idade == 18:
    print('Já é hora de se alistar!!!')
else:
    print('Já se passou {} anos do tempo de alistamento!'.format(idade-18))
