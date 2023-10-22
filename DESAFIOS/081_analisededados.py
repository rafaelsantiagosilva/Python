print(f'{"Exercício 81":-^50}')
opc = 'S'
nums = list()
c5 = 'não faz parte'
while opc == 'S':
    n = int(input('\nDigite um valor: '))
    nums.append(n)
    if n == 5:
        c5 = 'faz parte'
    opc = str(input('\nDeseja continuar? [S/N]\nR: ')).upper()
print(f'{"":-^50}')
print(f'Você digitou {len(nums)} elementos')
nums.sort(reverse=True)
print(f'Os valores em ordem decrescente são {nums}')
print(f'O valor 5 {c5} da lista!')
print(f'{"":-^50}')