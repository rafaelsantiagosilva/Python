print(f'{"Aula 16: Tuplas":-^50}')

# Tuplas são imutáveis (constantes)
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita', 'Açaí')
#               0          1        2        3

# Imprimindo a tupla inteira
print('Tupla:', lanche)

# Segundo elemento
print('\nSegundo elemento:', lanche[1])

# Penúltimo elemento
print('Segundo elemento, do fim ao inicio (penúltimo):', lanche[-2])

# De tal até tal mas desconsidera o ultimo valor
print('\nDe tal até tal:', lanche[0:3])

# De tal pra frente
print('De tal pra frente:', lanche[1:])

# De tal para trás mas desconsiderando o inicial
print('De tal para trás:', lanche[:2])

# Imprimindo com o for
for comida in lanche:
    print(f'\nEu vou comer: {comida}')
print('\nCOMI MUITO!\n')

# Imprimindo com posição de forma convencional
for i in range(0, len(lanche)):
    print(f'{i+1}º foi o(a) {lanche[i]}')

print('\nOU\n')

# Imprimindo com posição forma Python
for pos, comida in enumerate(lanche):
    print(f'{pos+1}º foi o(a) {comida}')
    
# Imprimindo tamanho da tupla
print(f'\n{len(lanche)} coisas é muito?')

# Imprimindo em ordem alfabética
print(sorted(lanche))