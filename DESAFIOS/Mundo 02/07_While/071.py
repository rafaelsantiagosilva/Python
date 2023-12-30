print(f'{"Exercício 71":-^50}')
print(f'{"":-^45}\n{"BANCO CEV":^45}\n{"":-^45}')
v = int(input('OBS:\nNotas disponíveis: R$50, R$20, R$10 e R$1\nDigite o valor a ser sacado: R$'))
n50 = v//50
n20 = (v - n50 * 50)//20
n10 = (v - n50 * 50 - n20 * 20)//10
n1 = (v - n50 * 50 - n20 * 20 - n10 * 10)
print('\nTotal de notas:')
if n50 != 0:
    print(f'R$50: {n50}')
if n20 != 0:
    print(f'R$20: {n20}')
if n10 != 0:
    print(f'R$10: {n10}')
if n1 != 0:
    print(f'R$1: {n1}')
print(f'{"":-^45}')