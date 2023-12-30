print(f'{"Exercício 78":-^50}')
print('Digite 5 valores numéricos: ')

valores = list()
maior = menor = 0
pos_maior = list()
pos_menor = list()

for i in range(0, 5):
    valores.append(float(input(f"{i+1}º valor:")))
    if i == 0:
        maior = valores[i]
        menor = valores[i]
    else:
        if valores[i] >= maior:
            maior = valores[i]
        if valores[i] <= menor:
            menor = valores[i]

for i in range(0, len(valores)):
    if valores[i] == maior:
        pos_maior.append(i+1)
    if valores[i] == menor:
        pos_menor.append(i+1)
        
print(f'\nO maior valor é {maior} e está na posição {pos_maior}')
print(f'O menor valor é {menor} e está na posição {pos_menor}')