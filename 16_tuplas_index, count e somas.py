print(f'{"Aula 16: Tuplas":-^50}')

a = (2, 5, 4)
b = (5, 8, 1, 2)

# "Concatenando" tuplas
print(a+b)
print(b+a)

c = b + a

# Contando quantos 5s tem
print(c.count(5))

# Vendo a posição de onde está o 8
print(c)
print(c.index(8))

# Vendo a posição da PRIMEIRA VEZ que aparece o 2
print(c.index(2))

# # Vendo a posição da PRIMEIRA VEZ que aparece o 2 a partir da posição 4
print(c.index(2, 4))