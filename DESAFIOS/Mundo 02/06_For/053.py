print('{:-^50}'.format('Exercício 53'))
frase = str(input('Digite uma frase: \n')).strip().upper()
frase = frase.split()
frase_junta = ''.join(frase)
frase_contraria = ''
for i in range(len(frase_junta)-1, -1, -1):
    frase_contraria+=frase_junta[i]
if frase_junta == frase_contraria:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
