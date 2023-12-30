print(f'{"Exercício 82":-^50}')
expressao = str(input('Digite a expressão matemática: '))
# Contabilizando parenteses
parenteses = 0
for i in range(0, len(expressao)):
    if expressao[i] == '(':
        parenteses+=1
    if expressao[i] == ')':
        if parenteses > 0:
            parenteses -= 1
        else:
            parenteses += 1
            break
if parenteses > 0:
    print('Expressão inválida')
else:
    print('Expressão válida')