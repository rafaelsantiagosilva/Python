print(f'{"Aula 17":-^50}')
lanche = ["Hamburguer", 'Suco', 'Pizza', 'Picolé']
print(lanche)

# Adicionando um valor ao final da lista
lanche.append("Cookie")
print(lanche)

# Adicionando em primeiro
lanche.insert(0, 'Cachorro Quente')
print(lanche)

# Apagando o último elemento
lanche.pop()
print(lanche)

# Apagando um elemento pelo indice
del lanche[2]
print(lanche)

# Apagando um elemento pelo valor
if 'Pizza' in lanche:
    lanche.remove('Pizza')
print(lanche)

# Lendo Valores
lista3 = list()
for i in range(0, 5):
    lista3.append(int(input("Digite um valor: ")))

# Mostrando valores
for i in range(0, len(lista3)):
    print(f'{lista3[i]}...', end='')