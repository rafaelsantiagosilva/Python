print('{:-^50}'.format('Exercício 57'))
sexo = str(input('Informe seu sexo[M/F]: ')).upper()
while not sexo in 'MF':
    sexo = str(input('ERRO: Informe novamente: ')).upper()
print('Vlw :D')