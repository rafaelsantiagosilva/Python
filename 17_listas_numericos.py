print(f'{"Aula 17":-^50}')

# Criando de um jeito mais rápido a lista
lista1 = list(range(0, 11, 2)) # De 0 até 11-1, pulando de 2 em 2
print(lista1)

lista2 = [8, 2, 5, 4, 9, 3, 0]
print(lista2)

# Ordenando em ordem crescente
lista2.sort()
print(lista2)

# Ordenando em ordem decrescente
lista2.sort(reverse=True)
print(lista2)

# Tamanho da lista
print(len(lista2))