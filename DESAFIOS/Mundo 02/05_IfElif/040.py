print("{:-^40}".format('Exercício 40'))
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
print('\n{:-^40}'.format('MÉDIA'))
media = (nota1+nota2)/2
if media >= 7.0:
    condicao = 'APROVADO'
elif media >= 5.0 and media <= 6.9:
    condicao = 'RECUPERAÇÃO'
else:
    condicao = 'REPROVADO'
print('{} -> {}'.format(media, condicao))
print('{:-^40}'.format(''))