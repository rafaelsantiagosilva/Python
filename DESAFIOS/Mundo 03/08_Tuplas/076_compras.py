print(f'{"Exercício 76":-^50}')
lista = ('Pão', 1, 'Leite', 3.50, 'Frango', 21.75, 'Pizza Congelada', 10.99)
print(f'\n{"":=^45}\n{"ITENS":^45}\n{"":=^45}')
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:-<35}R${lista[i+1]}')
print(f'{"":=^45}')