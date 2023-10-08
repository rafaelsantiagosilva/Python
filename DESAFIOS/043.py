print("{:-^40}".format('Exercício 43'))
peso = float(input('Digite seu peso [kg]: '))
altura = float(input('Digite sua altura [m]: '))
imc = peso/(altura*altura)
print('{:-^40}'.format('IMC'))
if imc < 18.5:
    condicao = 'ABAIXO DO PESO'
elif imc >= 18.5 and imc <= 25.0:
    condicao = 'PESO IDEAL'
elif imc >= 25.0 and imc <= 30.0:
    condicao = 'SOBREPESO'
elif imc >= 30.0 and imc <= 40.0:
    condicao = 'OBESIDADE'
else:
    condicao = 'OBESIDADE MÓRBIDA'
print('{} -> {}'.format(imc, condicao))
print('{:-^40}'.format(''))