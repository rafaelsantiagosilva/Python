print(f'{"Aula 17":-^50}')
a = [1, 2, 3, 4]

# Ligação de listas
b = a
print(a, b)

    # Muda nas duas listas
b[2] = 7
print(a, b)
a[2] = 3

# Cópias de listas
c = a[:]
c[3] = 6
print(a, c)