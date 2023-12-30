print(f'{"Exercício 80":-^50}')
print('Digite 5 valores:')
lista = []
for i in range(0, 5):
    n = int(input(f'{i+1}ºvalor: '))
    if i == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(lista)