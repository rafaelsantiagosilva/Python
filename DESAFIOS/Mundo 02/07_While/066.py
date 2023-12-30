print('{:-^50}'.format('Exercício 66'))
n = c = s = 0
while True:
    n = int(input('Digite um número[999 para parar]:'))
    if n == 999:
        break
    c+=1
    s+=n
print(f'A soma entre os {c} números digitados foi de {s}')