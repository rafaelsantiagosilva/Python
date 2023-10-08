import datetime
print("{:-^40}".format('Exercício 41'))
ano_atual = datetime.datetime.now().year
ano_nasc_atleta = int(input('Digite o ano em que o atleta nasceu: '))
idade = ano_atual - ano_nasc_atleta
if idade <= 9.0:
    categoria = 'MIRIM'
elif idade <= 14.0:
    categoria = 'INFANTIL'
elif idade <= 19.0:
    categoria = 'JUNIOR'
elif idade <= 20.0:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print('\n{:-^40}'.format('CATEGORIA DO ATLETA'))
print('{:^40}'.format(categoria))
print('{:-^40}'.format(''))
