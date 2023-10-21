print(f'{"Exercício 76":-^50}')
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'ESTUDAR', 'CURSO', 'GRATIS', 'PIZZA', 'JAVA')
vogais = ('a', 'e', 'i', 'o', 'u')
for i in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[i]} temos: ', end='')
    for j in range(0, len(palavras[i])):
        if palavras[i][j] in 'AEIOU':
            print(f'{palavras[i][j]} '.lower(), end='')